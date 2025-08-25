<h1 align="center">🔐 SecureOne Bot</h1>
<p align="center">A secure Telegram bot for managing and encrypting your passwords with ease.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Telegram-lightgrey?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Security-Encrypted-green?style=flat-square" />
</p>

---

## 📑 Table of Contents

- [✨ Overview](#-overview)
- [🚀 Features](#-features)
- [🤔 Why This Project](#-why-this-project)
- [⚙️ How It Works](#️-how-it-works)
- [🛠️ Installation](#️-installation)
- [🎮 Usage](#-usage)
- [📂 Project Structure](#-project-structure)
- [🔐 Security Considerations](#-security-considerations)
- [⚠️ Disclaimer](#️-disclaimer)
- [📄 License](#-license)

---

## ✨ Overview

**SecureOne Bot** is a Telegram bot designed to act as a lightweight, encrypted password manager.  
It allows users to securely store, retrieve, and manage sensitive data (like login credentials) directly within Telegram — all protected with **Fernet encryption** from the `cryptography` library.  

This project was built as a **practical security tool** and as a learning project to explore:
- Cryptography in Python  
- Telegram Bot API  
- Secure storage & password management  

---

## 🚀 Features

- 🔑 **Password Vault** – Save, retrieve, and delete passwords securely.  
- 🔒 **Encryption** – All stored passwords are encrypted with Fernet.  
- 👤 **User-Specific Storage** – Each Telegram user manages their own encrypted data.  
- 💾 **Persistent Storage** – Data saved in JSON file (can be upgraded to database).  
- 🖥️ **Simple UI** – Easy-to-use inline buttons in Telegram.  
- 🛡️ **Security First** – Sensitive information is never stored in plain text.  

---

## 🤔 Why This Project

Most students make “To-Do List” or “Calculator” projects.  
This project stands out because it solves a **real-world problem** → password management with encryption.  

It also helped me learn:
- API integration (Telegram)  
- Practical encryption methods  
- Secure handling of sensitive data  
- Building user-friendly bots  

---

## ⚙️ How It Works

1. User interacts with the bot via Telegram.  
2. Bot generates a unique encryption key and securely stores passwords.  
3. Data is saved in encrypted form inside a JSON file.  
4. When requested, bot decrypts and shows the data to the correct user only.  

---

## 🛠️ Installation

### 🔧 Prerequisites
- Python 3.10 or higher  
- A [Telegram Bot Token](https://core.telegram.org/bots/tutorial#getting-ready) from @BotFather  

### 📥 Steps

```bash
# Clone the repo
git clone https://github.com/retarduser404/telegrambot.git

# Navigate to the project directory
cd telegrambot

# Install requirements
pip install -r requirements.txt

# Run the bot
python main.py
````

---

## 🎮 Usage

1. Open Telegram and start the bot (`/start`).
2. Use inline buttons to add, retrieve, or delete stored credentials.
3. All data is encrypted automatically.
4. Enjoy secure password management directly in Telegram!

---

## 📂 Project Structure

```
telegrambot/
│-- main.py              # Entry point of the bot
│-- requirements.txt     # Python dependencies
│-- data.json            # Encrypted user data storage
│-- utils/               # Helper functions (encryption, validation, etc.)
│-- README.md            # Project documentation
```

---

## 🔐 Security Considerations

* Passwords are encrypted using **Fernet (symmetric encryption)**.
* No plain-text credentials are stored.
* Each user’s data is stored separately for isolation.
* 🔮 Future upgrades:

  * Use **SQLite/Postgres DB** instead of JSON.
  * Add **multi-factor authentication (MFA)**.
  * Dockerize the project for deployment.

---

## ⚠️ Disclaimer

⚠️ This bot is built for **educational purposes only**.
It is **not recommended** for storing highly sensitive or production-grade credentials.
Use at your own risk.

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use, modify, and share.

---

🚀 *SecureOne Bot — because your passwords deserve better security.*
