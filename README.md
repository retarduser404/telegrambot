🔐 SecureOne Password Vault Bot

Boost your privacy, manage your credentials, and generate strong passwords — all inside Telegram!


📑 Table of Contents

🔎 Overview

✨ Features

⚙️ Installation

🖥️ Usage

📂 Project Structure

🛡 Security Disclaimer

📜 License

🔎 Overview

SecureOne Bot is a Telegram-based password vault that helps you:

Securely store and retrieve credentials

Keep data encrypted using cryptography.Fernet

Manage entries with simple Telegram commands

⚠️ Built for educational purposes only — not a production-grade password manager.

✨ Features

🔑 Encrypted Storage → All usernames & passwords encrypted with Fernet

👤 User Registration → Only confirmed users can save/retrieve data

📝 Password Management → Add, update, delete, and list entries

⚡ Strong Password Generator → Generate secure random passwords

📲 Inline Copy Buttons → Tap to copy credentials instantly

🗂 Simple JSON Storage → Lightweight and beginner-friendly

⚙️ Installation
📌 Prerequisites

Python 3.10 or higher

A Telegram Bot Token (from @BotFather
)

🚀 Steps
# 1. Clone the repo
git clone https://github.com/<your-username>/secureone-password-vault-bot.git
cd secureone-password-vault-bot

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with your bot credentials
echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env
echo "OWNER_TELEGRAM_ID=your_user_id" >> .env

# 5. Run the bot
python bot.py

🖥️ Usage
⌨️ Commands

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


.gitignore

.env
*.json
*.key
__pycache__/

🛡 Security Disclaimer

Uses a single encryption key (key.key) → if leaked, all data is exposed

Data stored in JSON files → okay for demo, unsafe for production

Telegram bots are not end-to-end encrypted → not ideal for sensitive secrets

Intended as a learning project, not as a professional vault replacement

📜 License

This project is licensed under the MIT License.
