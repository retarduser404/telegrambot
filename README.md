<h1 align="center">🔐 SecureOne - Password Vault Bot</h1>
<p align="center">A secure Telegram-based password manager — store, manage, and retrieve your credentials safely with encryption!</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Telegram-lightgrey?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" />
</p>

---

## 📑 Table of Contents

- [✨ Overview](#-overview)
- [🚀 Features](#-features)
- [🛠️ Installation](#️-installation)
- [🎮 Usage](#-usage)
- [🧪 Testing](#-testing)
- [📄 License](#-license)

---

## ✨ Overview

**SecureOne** is a **Telegram-based password vault bot** built in Python.  
It allows users to securely **store, manage, and retrieve credentials** directly inside Telegram.  
Your data is **encrypted with Fernet cryptography**, ensuring that sensitive information stays private.  

This project was created to demonstrate **data security, bot development, and encryption** in a beginner-friendly way.  

---

## 🚀 Features

- 🔑 **Encrypted Storage:** All passwords stored with strong Fernet encryption.  
- 👤 **User Authentication:** Register & confirm before accessing the vault.  
- ➕ **CRUD Operations:** Add, update, delete, and retrieve credentials.  
- 🎲 **Password Generator:** Built-in strong random password generator.  
- 💾 **Lightweight Database:** JSON file-based storage (easy to use, no setup).  
- 🤖 **Telegram Bot:** Fully interactive CLI-like experience in chat.  
- 🧼 **Clean & Modular Codebase:** Easy to understand, extend, and customize.  

---

## 🛠️ Installation

### 🔧 Prerequisites

- Python **3.10+**  
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))  

### 📥 Steps

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/SecureOne-Bot.git

# Navigate to the project directory
cd SecureOne-Bot

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
