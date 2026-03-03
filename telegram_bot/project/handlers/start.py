import logging
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def start(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        user_name = update.effective_user.first_name

        if 'first_time' not in context.user_data:
            context.user_data['first_time'] = True
            await update.message.reply_text(get_text_for_user(user_id, 'start').format(user_name=user_name))
            logger.info(f'👤 New user: {user_name}, ({user_id})')

        else:
            await update.message.reply_text(get_text_for_user(user_id, 'start_again').format(user_name=user_name))
            logger.info(f'👤 Returning user {user_id}')

    except Exception as e:
        logger.error(f'❌ Error in start: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')