import logging
from logging.handlers import RotatingFileHandler
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers.start import start
from handlers.help import help_command
from handlers.mode import mode_command
from handlers.echo import echo
from handlers.admin_help import admin_help
from handlers.admin_stats import admin_stats
from handlers.admin_user_info import admin_user_info
from handlers.admin_ban import admin_ban
from handlers.admin_unban import admin_unban
from config_loader import load_config
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            'logs/bot.log',
            maxBytes=5*1024*1024,
            backupCount=3,
            encoding='utf-8'
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger('telegram').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

config = load_config()
if config.get('bot_token') == 'YOUR_BOT_TOKEN_HERE':
    logger.error("❌ Bot token isn't set in config.json")
    exit(1)

async def error_callback(update, context):
    logger.error(f'Update caused error: {context.error}')

def main():
    try:
        app = Application.builder().token(config.get('bot_token')).build()
        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('mode', mode_command))
        app.add_handler(CommandHandler('admin_help', admin_help))
        app.add_handler(CommandHandler('admin_stats', admin_stats))
        app.add_handler(CommandHandler('admin_user_info', admin_user_info))
        app.add_handler(CommandHandler('admin_ban', admin_ban))
        app.add_handler(CommandHandler('admin_unban', admin_unban))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        app.add_error_handler(error_callback)
        
        logger.info('✅ Bot started')
        app.run_polling()
        
    except Exception as e:
        logger.error(f'❌ Critical error: {e}')

if __name__ == '__main__':
    main()