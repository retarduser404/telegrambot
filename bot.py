"""
SecureOne Password Vault Bot
============================
A Telegram bot to store encrypted passwords per user.
Secrets (BOT_TOKEN, OWNER_TELEGRAM_ID) are loaded from .env file.
"""

import os
import json
import secrets
from cryptography.fernet import Fernet
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
)
from dotenv import load_dotenv

# === LOAD ENVIRONMENT ===
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_TELEGRAM_ID")

if not BOT_TOKEN:
    raise EnvironmentError("❌ TELEGRAM_BOT_TOKEN is missing. Add it in your .env file.")
if not OWNER_ID:
    raise EnvironmentError("❌ OWNER_TELEGRAM_ID is missing. Add it in your .env file.")

# === FILE CONFIG ===
DATA_FILE = "passwords.json"
USERS_FILE = "users.json"
KEY_FILE = "key.key"

# === ENCRYPTION ===
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt(text: str) -> str:
    return Fernet(load_key()).encrypt(text.encode()).decode()

def decrypt(token: str) -> str:
    return Fernet(load_key()).decrypt(token.encode()).decode()

# === USER MANAGEMENT ===
def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def is_registered(user_id):
    return str(user_id) in load_users()

def register_user(user_id):
    users = load_users()
    uid = str(user_id)
    if uid not in users:
        users.append(uid)
        save_users(users)

# === STORAGE HELPERS ===
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_user_data(uid):
    data = load_data()
    return data.get(str(uid), {})

def set_user_data(uid, user_data):
    data = load_data()
    data[str(uid)] = user_data
    save_data(data)

# === COMMANDS ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 Welcome to SecureOne Password Vault Bot!\nUse /register to get started.")

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Your Telegram ID is: {user_id}\nSend /confirm {user_id} to register.")

async def confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or args[0] != str(update.effective_user.id):
        await update.message.reply_text("❌ Invalid ID. Please use /confirm <your_telegram_id>")
        return
    register_user(update.effective_user.id)
    await update.message.reply_text("✅ You are now registered! Use /add to begin saving passwords.")

async def require_registration(update: Update):
    if not is_registered(update.effective_user.id):
        await update.message.reply_text("❌ You're not registered. Use /register first.")
        return False
    return True

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await require_registration(update): return
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Usage: /add <key> <username> <password>")
        return
    key, username, password = args[0], args[1], " ".join(args[2:])
    user_id = update.effective_user.id
    data = get_user_data(user_id)
    data[key] = {
        "username": encrypt(username),
        "password": encrypt(password)
    }
    set_user_data(user_id, data)
    await update.message.reply_text(f"✅ Saved entry for '{key}'.")

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await require_registration(update): return
    args = context.args
    if len(args) != 1:
        await update.message.reply_text("Usage: /get <key>")
        return
    key = args[0]
    user_id = update.effective_user.id
    data = get_user_data(user_id)
    if key in data:
        creds = data[key]
        username = decrypt(creds['username'])
        password = decrypt(creds['password'])
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔑 Copy Password", callback_data=f"copy|{password}")]])
        await update.message.reply_text(
            f"🔐 <b>{key}</b>\n👤 {username}\n\nTap to copy password.",
            parse_mode="HTML",
            reply_markup=keyboard
        )
    else:
        await update.message.reply_text(f"❌ No entry found for '{key}'.")

async def update_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await require_registration(update): return
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Usage: /update <key> <username> <password>")
        return
    key, username, password = args[0], args[1], " ".join(args[2:])
    user_id = update.effective_user.id
    data = get_user_data(user_id)
    if key in data:
        data[key] = {
            "username": encrypt(username),
            "password": encrypt(password)
        }
        set_user_data(user_id, data)
        await update.message.reply_text(f"✅ Updated entry for '{key}'.")
    else:
        await update.message.reply_text(f"❌ No entry found for '{key}'.")

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await require_registration(update): return
    args = context.args
    if len(args) != 1:
        await update.message.reply_text("Usage: /delete <key>")
        return
    key = args[0]
    user_id = update.effective_user.id
    data = get_user_data(user_id)
    if key in data:
        del data[key]
        set_user_data(user_id, data)
        await update.message.reply_text(f"🗑️ Deleted entry '{key}'.")
    else:
        await update.message.reply_text(f"❌ No entry found for '{key}'.")

async def list_keys(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await require_registration(update): return
    data = get_user_data(update.effective_user.id)
    if not data:
        await update.message.reply_text("🔍 No saved entries.")
        return
    keys = "\n".join(f"• {k}" for k in data.keys())
    await update.message.reply_text(f"📁 Saved keys:\n{keys}")

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await require_registration(update): return
    length = 16
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("📋 Copy Password", callback_data=f"copy|{password}")]])
    await update.message.reply_text(
        f"🔧 Generated Password: <code>{password}</code>",
        parse_mode="HTML",
        reply_markup=keyboard
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query: return
    await query.answer()
    if query.data.startswith("copy|"):
        password = query.data.split("|", 1)[1]
        await query.edit_message_text(f"🔑 <code>{password}</code>", parse_mode="HTML")

# === MAIN ===
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    await app.bot.set_my_commands([
        BotCommand("start", "Start the bot"),
        BotCommand("register", "Show your Telegram ID"),
        BotCommand("confirm", "Confirm registration"),
        BotCommand("add", "Add a password"),
        BotCommand("get", "Retrieve a password"),
        BotCommand("update", "Update a password"),
        BotCommand("delete", "Delete a password"),
        BotCommand("list", "List saved keys"),
        BotCommand("generate", "Generate strong password"),
    ])

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("confirm", confirm))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("get", get))
    app.add_handler(CommandHandler("update", update_entry))
    app.add_handler(CommandHandler("delete", delete))
    app.add_handler(CommandHandler("list", list_keys))
    app.add_handler(CommandHandler("generate", generate))
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("✅ Bot is running with public registration and encryption...")
    await app.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    import asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())
