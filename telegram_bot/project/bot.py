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
from handlers.remind import remind
from handlers.reminders import reminders
from handlers.remove_reminder import remove_reminder_handler
from utils.reminder_scheduler import check_and_send_reminders
from config_loader import load_config
import os
import glob
import shutil
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"📁 Working directory: {script_dir}")

for folder in ['data', 'logs', 'backups']:
    os.makedirs(folder, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
files_to_backup = ['data/reminders.json', 'data/users.json']

for file_path in files_to_backup:
    if os.path.exists(file_path):
        backup_name = f'backups/{os.path.basename(file_path)}_{timestamp}.json'
        shutil.copy2(file_path, backup_name)
        print(f'✅ Backup created: {backup_name}')
    
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('{}')
        print(f'📄 Created empty file: {file_path}')
    
backup_files = sorted(glob.glob('backups/*.json'), key=os.path.getmtime)

if len(backup_files) > 10:
    for old_backup in backup_files[:-10]:
        os.remove(old_backup)
        print(f'🗑️ Deleted old backup: {os.path.basename(old_backup)}')

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
logging.getLogger('apscheduler').setLevel(logging.WARNING)

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

        job_queue = app.job_queue
        job_queue.run_repeating(callback=check_and_send_reminders, interval=300, first=10)

        app.add_handler(CommandHandler('start', start))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('mode', mode_command))
        app.add_handler(CommandHandler('admin_help', admin_help))
        app.add_handler(CommandHandler('admin_stats', admin_stats))
        app.add_handler(CommandHandler('admin_user_info', admin_user_info))
        app.add_handler(CommandHandler('admin_ban', admin_ban))
        app.add_handler(CommandHandler('admin_unban', admin_unban))
        app.add_handler(CommandHandler('remind', remind))
        app.add_handler(CommandHandler('reminders', reminders))
        app.add_handler(CommandHandler('remove_remind', remove_reminder_handler))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
        app.add_error_handler(error_callback)
        
        logger.info('✅ Bot started')
        app.run_polling()
        
    except Exception as e:
        logger.error(f'❌ Critical error: {e}')

if __name__ == '__main__':
    main()