# Milrus Telegram Bot 🤖

A multifunctional Telegram bot with mirror mode, reminder system, and admin panel.

## ✨ Features

### 🎭 Working Modes
1. **Mirror Mode** 🔄 — Echoes your messages back to you
2. **Reminder Mode** ⏰ — Set recurring reminders with custom intervals (1-168 hours)
3. *More modes coming soon...*

### 📋 User Commands
- `/start` — Start the bot
- `/help` — Show help message
- `/mode` — Switch between modes
- `/remind [text] [hours]` — Create a reminder (1-168 hours)
- `/my_reminds` — List your reminders (max 5 per user)
- `/remove_remind [ID]` — Delete a reminder by ID

### 🔧 Admin Commands
- `/admin_help` — Admin help
- `/admin_stats` — Bot statistics
- `/admin_user_info [user_id]` — Get user info
- `/admin_ban [user_id] [reason]` — Ban a user
- `/admin_unban [user_id]` — Unban a user

## 🛠️ Technologies Stack
- **Python 3.11+** — Core language
- **python-telegram-bot** — Bot framework
- **JSON-based storage** — For reminders and user data
- **Rotating file logging** — Automatic log rotation
- **Git & GitHub** — Version control
- **VS Code** — Development environment

## 🚀 Quick Start

### 1. Installation
```bash
# Clone repository
git clone https://github.com/yourusername/telegram_bot.git
cd telegram_bot/project

# Install dependencies
pip install -r requirements.txt

# Copy config template
cp config_template.json config.json

# Edit config.json and add:
# - Your bot token from @BotFather
# - Your admin user ID

# Start the bot
python bot.py

# Edit config.json:

{
    "bot_token": "YOUR_BOT_TOKEN_HERE",
    "admin_ids": [123456789],
    "blacklist": []
}

# Logging:

Logs stored in data/logs/bot.log
Automatic rotation every 5MB
3 backup files kept
```

### 📊 Development Status:

**Current Version: 0.6.0**

### 👤 Developer:

**Milrus — Computer Science student**

*Updated January 27th, 2026*
