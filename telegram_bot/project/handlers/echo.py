import logging
from utils.user_manager import update_user
from utils.rate_limiter import limiter
from utils.safe_logger import safe_logger
from utils.validators import valid_len_text, no_binary

logger = logging.getLogger(__name__)

async def echo(update, context):
    try:
        user_text = update.message.text
        user_id = update.effective_user.id
        update_user(user_id)

        if not user_text.strip():
            await update.message.reply_text('📝 Please, type something')
            return

        if not valid_len_text(user_text, max_len=1000):
            await update.message.reply_text('❌ The message is too long (no more than 1000 characters)')
            logger.warning(f'Too long message from {user_id}: {len(user_text)} characters')
            return
        
        if not no_binary(user_text):
            await update.message.reply_text('❌ The message contains invalid characters')
            logger.warning(f'Binary characters from {user_id}')
            return

        if limiter(context.user_data, interval=1.0):
            await update.message.reply_text('⏳ Please, not so fast')
            logger.warning(f'The user {user_id} if sending messages too fast')
            return

        await update.message.reply_text(user_text)

        safe_text = safe_logger(user_text, max_len=200)
        logger.info(f'📨 Echo from user {user_id}: "{safe_text}"')

    except Exception as e:
        logger.error(f'❌ Error in echo: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')