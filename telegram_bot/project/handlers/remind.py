import logging
from utils.reminder_storage import add_reminder
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def remind(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if len(context.args) < 2:
            await update.message.reply_text(get_text_for_user(user_id, 'remind_no_context_args'))
            return
        
        try:
            hours = int(context.args[-1])

        except ValueError:
            await update.message.reply_text(get_text_for_user(user_id, 'remind_incorrect_hours'))
            return
        
        except IndexError:
            await update.message.reply_text(get_text_for_user(user_id, 'remind_no_hours'))
            return

        text = ' '.join(context.args[:-1])

        if not (1 <= hours <= 168):
            await update.message.reply_text(get_text_for_user(user_id, 'remind_incorrect_range'))
            return

        if not text.strip():
            await update.message.reply_text(get_text_for_user(user_id, 'remind_no_text'))
            return
        
        if len(text) > 1000:
            await update.message.reply_text(get_text_for_user(user_id, 'remind_incorrect_len'))
            return

        user_id = update.effective_user.id

        reminder_id = add_reminder(user_id, text, hours)

        if reminder_id:
            logging.info(f'📝 The user {user_id} added a new reminder (ID: {reminder_id})')
            await update.message.reply_text(get_text_for_user(user_id, 'reminder_added').format(reminder_id=reminder_id))
        else:
            await update.message.reply_text(get_text_for_user(user_id, 'reminders_limit'))
    
    except Exception as e:
        logger.error(f'❌ Error in remind: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))