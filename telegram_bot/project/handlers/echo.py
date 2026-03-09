import logging
from utils.user_manager import update_user
from utils.rate_limiter import limiter
from utils.safe_logger import safe_logger
from utils.validators import valid_len_text, no_binary
from utils.user_manager import increase_spam_flags
from utils.ban_manager import check_autoban, is_user_banned
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def echo(update, context):
    try:
        user_text = update.message.text
        user_id = update.effective_user.id
        update_user(user_id)

        if is_user_banned(user_id):
            await update.message.reply_text(get_text_for_user(user_id, 'echo_banned_user'))
            logger.info(f'⛔ Banned user {user_id} attempted to use echo')
            return
        
        if not user_text.strip():
            await update.message.reply_text(get_text_for_user(user_id, 'echo_not_user_text'))
            return

        if not valid_len_text(user_text, max_len=1000):
            await update.message.reply_text(get_text_for_user(user_id, 'echo_invalid_len'))
            logger.warning(f'Too long message from {user_id}: {len(user_text)} characters')
            return
        
        if not no_binary(user_text):
            await update.message.reply_text(get_text_for_user(user_id, 'echo_invalid_chars'))
            logger.warning(f'Binary characters from {user_id}')
            return

        if limiter(context.user_data, interval=1.0):
            await update.message.reply_text(get_text_for_user(user_id, 'echo_limit'))

            updated_users = increase_spam_flags(user_id)

            if check_autoban(user_id, updated_users):
                await update.message.reply_text(get_text_for_user(user_id, 'echo_ban_spam'))
                logger.warning(f'🚫 User {user_id} had been banned for spam by autoban')
                return
            
            logger.warning(f'The user {user_id} if sending messages too fast')
            return

        await update.message.reply_text(user_text)

        safe_text = safe_logger(user_text, max_len=200)
        logger.info(f'📨 Echo from user {user_id}: "{safe_text}"')

    except Exception as e:
        logger.error(f'❌ Error in echo: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))