import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config_loader import load_config

logging.basicConfig(level=logging.INFO)

config = load_config()
if config.get('bot_token') == 'YOUR_BOT_TOKEN_HERE':
    print('WARNING: token is not loaded. Install it')
    exit(1)

async def start(update, context):
    chat_id = update.effective_chat.id
    if 'first_time' not in context.user_data:
        context.user_data['first_time'] = True
        await update.message.reply_text("Hello! I'm Milrus bot. You are currently in mirror mode")
    else:
        await update.message.reply_text('Hello again:)')

async def echo(update, context):
    user_text = update.message.text
    await update.message.reply_text(user_text)

async def help_command(update, context):
    await update.message.reply_text("""
    I'm Milrus, your helper bot!

Working Modes:
1) Mirror Mode 🔄 — I reply to your messages with the same text
2) Reminder Mode ⏰ (in development) — You enter reminder text and time, I'll notify you
3) Other modes 🛠️ — also in development...
                                    
Commands:
/start — Start the bot
/help — Show this help message
/mode — Switch between modes
                                    
Version: 0.1 | Developer: Milrus""")

def main():
    app = Application.builder().token(config.get('bot_token')).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == '__main__':
    main()