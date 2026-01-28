import logging
from datetime import datetime, timezone
from utils.reminder_storage import load_reminders, save_reminders

logger = logging.getLogger(__name__)

async def check_and_send_reminders(context):
    reminders = load_reminders()
    curr_time = datetime.now(timezone.utc)

    updated_reminders = {}

    for user_id_str, user_reminders_list in reminders.items(): 
        remaining_reminders = []

        for reminder in user_reminders_list:
            next_run = datetime.fromisoformat(reminder['next_run'])
            
            if next_run <= curr_time:
                    
                try:
                    await context.bot.send_message(chat_id=int(user_id_str), text=f"🔔 Reminder: {reminder['text']}")
                    logger.info(f"📨 Reminder {reminder['id']} sent to user {user_id_str}")
                    
                except Exception as e:
                    logger.warning(f'❌ Failed to send a reminder to user {user_id_str}: {e}')
                    remaining_reminders.append(reminder)

            else:
                remaining_reminders.append(reminder)

        if remaining_reminders:
            updated_reminders[user_id_str] = remaining_reminders

    save_reminders(updated_reminders)