import logging
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def mode_command(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        await update.message.reply_text(get_text_for_user(user_id, 'mode'))
        logger.info(f'🎛️  Mode requested by {update.effective_user.id}')

    except Exception as e:
        logger.error(f'❌ Error in mode: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))