# Telegram Group Chat Moderation Bot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![pyTelegramBotAPI](https://img.shields.io/badge/TelegramBotAPI-4.12%2B-blue.svg)](https://github.com/eternnoir/pyTelegramBotAPI)

A lightweight Telegram group chat moderation bot designed to assist chat administrators with role permission checks, user management, and automated ban execution.

---

## 🚀 Key Features

* **Role & Permission Verification**: Validates issuer admin privileges before executing moderation actions.
* **Admin Protection**: Prevents accidental ban attempts against group owners and administrators.
* **Reply-Based Command Handling**: Executes target bans by replying directly to problematic messages.
* **Exception Handling**: Gracefully handles Telegram API exceptions and missing user attributes.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: pyTelegramBotAPI

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/telegram-moderation-bot.git
cd telegram-moderation-bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure Credentials
Copy `config.py.example` to `config.py` and insert your Telegram Bot Token:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
