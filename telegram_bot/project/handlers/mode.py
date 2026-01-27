import logging

logger = logging.getLogger(__name__)

async def mode_command(update, context):
    try:
        mode_text = ('''🎭 Current bot mode:
HYBRID (all features active)\n
✅ Mirror Mode: Always ON
✅ Reminder Mode: Always ON
✅ Admin Panel: Available to admins\n
⚙️ All features work simultaneously.'''
        )
        await update.message.reply_text(mode_text)
        logger.info(f'🎛️  Mode requested by {update.effective_user.id}')

    except Exception as e:
        logger.error(f'❌ Error in mode: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')