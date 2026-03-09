import logging
from utils.admin_check import is_admin
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def help_command(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        await update.message.reply_text(get_text_for_user(user_id,'help'))
        logger.info(f'❓ Help requested by {user_id}')

        if is_admin(user_id):
            logger.info(f'💡 Admin {user_id} received admin hint in /help')
            await update.message.reply_text(get_text_for_user(user_id, 'help_admin_hint'))
    except Exception as e:
        logger.error(f'❌ Error in help: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))