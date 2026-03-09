import logging
from utils.reminder_storage import remove_reminder
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def remove_reminder_handler(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not context.args:
            await update.message.reply_text(get_text_for_user(user_id, 'remove_reminder_no_context_args'))
            return
        
        try:
            reminder_id = int(context.args[0])

        except ValueError:
            await update.message.reply_text(get_text_for_user(user_id, 'remove_reminder_id_error'))
            return
        
        user_id = update.effective_user.id
        success = remove_reminder(user_id, reminder_id)

        if success:
            logger.info(f'🗑️ User {user_id} deleted reminder {reminder_id}')
            await update.message.reply_text(get_text_for_user(user_id, 'remove_reminder_success').format(reminder_id=reminder_id))
        
        else:
            await update.message.reply_text(get_text_for_user(user_id, 'remove_reminder_fail').format(reminder_id=reminder_id))
    
    except Exception as e:
        logger.error(f'❌ Error in remove_remind: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))