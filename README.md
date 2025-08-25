🔐 SecureOne Password Vault Bot






![secureone](https://github.com/user-attachments/assets/9cd50d96-993d-47f3-a29d-68dbd344a3bc)


A Telegram bot to securely store and manage passwords using encryption.
It acts as a lightweight password manager where each user can save, update, retrieve, and generate strong passwords directly inside Telegram.

📌 Why I Built This

To explore bot development with Telegram API

To learn secure password storage using cryptography.Fernet

To provide a simple password vault demo for students & developers

⚠️ Note: This project is for educational purposes and not a production-grade vault

✨ Features

🔑 Store encrypted passwords per user

🔐 Retrieve & decrypt credentials only for registered users

📝 Update or delete saved entries

📁 List saved keys

⚡ Generate strong random passwords

📲 Inline buttons to copy credentials

🔒 User registration system

⚠️ Security Disclaimer

Passwords are encrypted with a single key (key.key). If this file leaks, all stored data is compromised.

Stored in JSON files → fine for demo, but not secure for real production.

Telegram messages are not end-to-end encrypted for bots → avoid storing highly sensitive data.

Use this as a learning project, not as your primary password vault.

🚀 Getting Started
1. Clone this repo
git clone https://github.com/<your-username>/secureone-password-vault-bot.git
cd secureone-password-vault-bot

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create .env file

In the root folder, create a file named .env with the following:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OWNER_TELEGRAM_ID=your_telegram_user_id


Get your bot token from @BotFather

Get your Telegram user ID from @userinfobot

5. Run the bot
python bot.py

📖 Usage
Commands

/start → Start the bot

/register → Show your Telegram ID

/confirm <your_id> → Register yourself

/add <key> <username> <password> → Save credentials

/get <key> → Retrieve credentials

/update <key> <username> <password> → Update entry

/delete <key> → Delete entry

/list → Show all saved keys

/generate → Generate strong random password

📂 Project Structure
📦 secureone-password-vault-bot
 ┣ 📜 bot.py            # Main bot script
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 README.md         # Documentation
 ┣ 📜 .gitignore        # Ignore sensitive files
 ┗ 📜 .env (ignored)    # Bot token & secrets

.gitignore (example)
.env
*.json
*.key
__pycache__/

👨‍💻 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit PRs.

📜 License

This project is licensed under the MIT License – free to use, modify, and distribute.
