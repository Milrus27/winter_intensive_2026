import logging
from logging.handlers import RotatingFileHandler
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config_loader import load_config

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    'logs/bot.log',
    maxBytes=1024*1024,
    backupCount=3,
    encoding='utf-8'
)

console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt= '%Y-%m-%d %H:%M:%S'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

config = load_config()
if config.get('bot_token') == 'YOUR_BOT_TOKEN_HERE':
    logger.error("Bot token isn't set in config.json")
    exit(1)

logger.info('Bot starting...')

async def start(update, context):
    try:
        user_id = update.effective_user.id
        user_name = update.effective_user.first_name

        if 'first_time' not in context.user_data:
            context.user_data['first_time'] = True
            await update.message.reply_text(
                f"""Hello, {user_name}! I'm Milrus bot.
This bot has several different modes.
You are currently in mirror mode 🔄"""
            )
            logger.info(f'👤 New user: {user_name}, ({user_id})')
        else:
            await update.message.reply_text(f'Hello again, {user_name}:)')
            logger.info(f'👤 Returning user {user_id}')

    except Exception as e:
        logger.error(f'❌ Error in start: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')

async def error_callback(update, context):
    logger.error(f'Update {update} caused error {context.error}')

async def echo(update, context):
    try:

        user_text = update.message.text
        user_id = update.effective_user.id

        if not user_text.strip():
            await update.message.reply_text('📝 Please, type something')
            return

        await update.message.reply_text(user_text)
        logger.info(f'📨 Echo from user {user_id}: "{user_text}"')
    except Exception as e:
        logger.error(f'❌ Error in echo: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')

async def help_command(update, context):
    try:
        help_text = (
            """I'm Milrus, your helper bot!\n
Working Modes:\n
1) Mirror Mode 🔄 — I reply to your messages with the same text
2) Reminder Mode ⏰ (in development) — Set reminders for important tasks
3) Other modes 🛠️ — coming soon...\n
Commands:\n
/start — Start the bot
/help — Show this help message
/mode — Switch between modes\n
Version: 0.2.1 | Developer: Milrus"""
        )
        await update.message.reply_text(help_text)
        logger.info(f'❓ Help requested by {update.effective_user.id}')

    except Exception as e:
        logger.error(f'❌ Error in help: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')

async def mode_command(update, context):
    try:
        mode_text = (
        '''🎛️ Current Mode: Mirror 🔄\n
Available Modes:\n
1) Mirror Mode 🔄 — echoes your message
2) Reminder Mode ⏰ (in development) — set reminders
3) Other modes 🛠️ — coming soon...\n
Use buttons below to switch modes (soon)'''
        )
        await update.message.reply_text(mode_text)
        logger.info(f'🎛️  Mode requested by {update.effective_user.id}')

    except Exception as e:
        logger.error(f'❌ Error in mode: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')

def main():
    try:
        app = Application.builder().token(config.get('bot_token')).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('mode', mode_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        app.add_error_handler(error_callback)

        logger.info('Bot is running, Ctrl + C to stop')
        app.run_polling()

    except Exception as e:
        logger.info(f'❌ Error: {e}')
        print('Check logs/bot.log')

if __name__ == '__main__':
    main()