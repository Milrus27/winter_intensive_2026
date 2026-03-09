import logging
from datetime import datetime, timezone
from utils.reminder_storage import get_user_reminders
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

def format_reminder_time(iso_time_str):
    try:
        format = datetime.fromisoformat(iso_time_str)
        return format.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    except Exception:
        return iso_time_str

def decline_hours(hours):
    if hours % 10 == 1 and hours % 100 != 11:
        return 'час'
    elif 2 <= hours % 10 <= 4 and (hours % 100 < 10 or hours % 100 >= 20):
        return 'часа'
    else:
        return 'часов'

async def reminders(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        user_reminders = get_user_reminders(user_id)

        if not user_reminders:
            await update.message.reply_text(get_text_for_user(user_id, 'no_reminders'))
            return
        
        reminders_count = len(user_reminders)
        message = [get_text_for_user(user_id, 'reminders_message(count)').format(reminders_count=reminders_count)]

        for reminder in user_reminders:
            reminder_id = reminder['id']
            reminder_text = reminder['text']
            reminder_time = reminder['hours']

            reminder_next_run = format_reminder_time(reminder['next_run'])

            hours_eng = 's' if reminder_time != 1 else ''
            hours_rus = decline_hours(reminder_time)

            block_parts = [
            '====================================',
            get_text_for_user(user_id, 'reminder_block_id').format(reminder_id=reminder_id),
            get_text_for_user(user_id, 'reminder_block_text').format(reminder_text=reminder_text),
            get_text_for_user(user_id, 'reminder_block_hours').format(
            reminder_time=reminder_time,
            hours_eng=hours_eng,
            hours_rus=hours_rus),
            get_text_for_user(user_id, 'reminder_block_due').format(reminder_next_run=reminder_next_run),
            '====================================']

            message.append('')
            message.append('\n'.join(block_parts))
            
        message.append(get_text_for_user(user_id, 'reminder_block_help'))
        result = '\n'.join(message)
        await update.message.reply_text(result, parse_mode='HTML')
        logger.info(f'📋 The user {user_id} viewed reminders list')

    except Exception as e:
        logger.error(f'❌ Error in my_reminds: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))