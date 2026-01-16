import logging

logger = logging.getLogger(__name__)

async def echo(update, context):
    try:

        user_text = update.message.text
        user_id = update.effective_user.id

        if not user_text.strip():
            await update.message.reply_text('📝 Please, type something')
            return

        await update.message.reply_text(user_text)
        logger.info(f'📨 Echo from user {user_id}: "{user_text}"')
    except Exception as e:
        logger.error(f'❌ Error in echo: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')