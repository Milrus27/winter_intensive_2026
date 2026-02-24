import logging
from utils.reminder_storage import remove_reminder
from utils.user_manager import update_user

logger = logging.getLogger(__name__)

async def remove_reminder_handler(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not context.args:
            await update.message.reply_text('❌ Usage: /remove_remind [ID]\n📋 View ID: /reminders\n⏰ Create a reminder: /remind [text] [hours]')
            return
        
        try:
            reminder_id = int(context.args[0])

        except ValueError:
            await update.message.reply_text('❌ The ID must be a number')
            return
        
        user_id = update.effective_user.id
        success = remove_reminder(user_id, reminder_id)

        if success:
            logger.info(f'🗑️ User {user_id} deleted reminder {reminder_id}')
            await update.message.reply_text(f'✅ The reminder {reminder_id} has been deleted')
        
        else:
            await update.message.reply_text(f'❌ No reminder with ID {reminder_id} was found')
    
    except Exception as e:
        logger.error(f'❌ Error in remove_remind: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')
