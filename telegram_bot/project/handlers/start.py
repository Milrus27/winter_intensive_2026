import logging

logger = logging.getLogger(__name__)

async def start(update, context):
    try:
        user_id = update.effective_user.id
        user_name = update.effective_user.first_name

        if 'first_time' not in context.user_data:
            context.user_data['first_time'] = True
            await update.message.reply_text(
                f"""Hello, {user_name}! I'm Milrus bot.
This bot has several different modes.
You are currently in mirror mode 🔄"""
            )
            logger.info(f'👤 New user: {user_name}, ({user_id})')
        else:
            await update.message.reply_text(f'Hello again, {user_name}:)')
            logger.info(f'👤 Returning user {user_id}')

    except Exception as e:
        logger.error(f'❌ Error in start: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')