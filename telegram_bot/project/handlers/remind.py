import logging
from utils.reminder_storage import add_reminder

logger = logging.getLogger(__name__)

async def remind(update, context):
    try:
        if len(context.args) < 2:
            await update.message.reply_text('❌ To call the command: /remind [text] [hours]')
            return
        
        try:
            hours = int(context.args[-1])

        except ValueError:
            await update.message.reply_text('❌ The number of hours must be an integer number (1 - 168)')
            return
        
        except IndexError:
            await update.message.reply_text('❌ Please, specify hours')
            return

        text = ' '.join(context.args[:-1])

        if not (1 <= hours <= 168):
            await update.message.reply_text('❌ The time should be between 1 and 168 (hours)')
            return

        if not text.strip():
            await update.message.reply_text('❌ Please, enter the text for the reminder')
            return
        
        if len(text) > 1000:
            await update.message.reply_text('❌ The text should be less than 1000 characters long')
            return

        user_id = update.effective_user.id

        reminder_id = add_reminder(user_id, text, hours)

        if reminder_id:
            logging.info(f'📝 The user {user_id} added a new reminder (ID: {reminder_id})')
            await update.message.reply_text(f'📝 You are successfully added a new reminder\nID: {reminder_id}')
        else:
            await update.message.reply_text('❌ You have exceeded the 5 reminder limit. Delete at least one')
    
    except Exception as e:
        logger.error(f'❌ Error in remind: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')