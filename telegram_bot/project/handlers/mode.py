import logging

logger = logging.getLogger(__name__)

async def mode_command(update, context):
    try:
        mode_text = (
        '''🎛️ Current Mode: Mirror 🔄\n
Available Modes:\n
1) Mirror Mode 🔄 — echoes your message
2) Reminder Mode ⏰ (in development) — set reminders
3) Other modes 🛠️ — coming soon...\n
Use buttons below to switch modes (soon)'''
        )
        await update.message.reply_text(mode_text)
        logger.info(f'🎛️  Mode requested by {update.effective_user.id}')

    except Exception as e:
        logger.error(f'❌ Error in mode: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')