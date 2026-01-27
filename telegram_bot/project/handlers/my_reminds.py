import logging
from utils.reminder_storage import get_user_reminders

logger = logging.getLogger(__name__)

async def my_reminds(update, context):
    try:
        user_id = update.effective_user.id
        user_reminders = get_user_reminders(user_id)

        if not user_reminders:
            await update.message.reply_text("📭 You don't have any reminders yet")
            return
        
        reminders_count = len(user_reminders)
        message = [f'📝 Your reminders ({reminders_count}/5):']

        for reminder in user_reminders:
            reminder_id = reminder['id']
            reminder_text = reminder['text']
            reminder_time = reminder['hours']
            reminder_next_run = reminder['next_run']

            reminder_block = f"""
==================
🔔 ID: {reminder_id}
📝 Text: {reminder_text}
⏰ Interval: every {reminder_time} hours
🕐 Next time: {reminder_next_run}
=================="""
    
            message.append(reminder_block)
        
        message.append('\n❓ To delete a reminder: /remove_remind [ID]')

        result = '\n'.join(message)
        await update.message.reply_text(result)
        logger.info(f'📋 The user {user_id} viewed reminders list')

    except Exception as e:
        logger.error(f'❌ Error in my_reminds: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')

        