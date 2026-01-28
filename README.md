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
- `/reminders` — List your reminders (max 5 per user)
- `/remove_remind [ID]` — Delete a reminder by ID

### 🔧 Admin Commands
- `/admin_help` — Admin help
- `/admin_stats` — Bot statistics
- `/admin_user_info [user_id]` — Get user info
- `/admin_ban [user_id] [reason]` — Ban a user
- `/admin_unban [user_id]` — Unban a user

## 🛠️ Technologies Stack
- **Python 3.11+** — Core language & asynchronous programming
- **python-telegram-bot** — Telegram Bot API framework
- **JSON-based storage** — User data and reminders persistence
- **Rotating file logging** — Automated log management (5MB rotation)
- **Linux (Mint) + Bash** — Development environment & system operations
- **Git & GitHub** — Version control & collaboration
- **VS Code** — IDE with Python tooling
- **VirtualBox** — Virtualization for Linux environment

## 💾 **Data Management & Backup**

### **Data Storage**
- **User data**: `data/users.json` - user statistics, ban status, message history
- **Reminders**: `data/reminders.json` - active reminders with timestamps in UTC
- **Format**: JSON files with UTF-8 encoding supporting Cyrillic/Unicode

### **Automatic Backup System**
- **Backup on startup**: Automatic backup of user data and reminders on every bot restart
- **Location**: `backups/` folder with timestamped files (e.g., `reminders_20260128_150000.json`)
- **Retention**: Keeps last 5 backups, automatically removes older ones
- **Manual restore**: Simply copy from `backups/` to `data/` folder if needed

### **Logging System**
- **Location**: `logs/bot.log` with automatic rotation
- **Rotation**: 5MB max size, keeps 3 backup log files
- **Format**: Human-readable with timestamps, log levels, and module names
- **Security**: Sensitive data (user IDs, message content) is logged securely

## 🛡️ **Security & Privacy**
- All times stored in UTC to avoid timezone issues
- Banned users can still use reminder functions (only echo mode restricted)
- Admin actions are logged for accountability

## 🚀 Quick Start

### 1. Installation
```bash
# Clone repository
git clone https://github.com/Milrus27/winter_intensive_2026.git
cd winter_intensive_2026/telegram_bot/project

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
```

### 📊 Development Status:

**Current Version: pre 1.0.0**

### 👤 Developer:

**Milrus — Computer Science student**

*Updated January 28th, 2026*
