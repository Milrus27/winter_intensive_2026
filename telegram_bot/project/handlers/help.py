import logging

logger = logging.getLogger(__name__)

async def help_command(update, context):
    try:
        help_text = (
            """I'm Milrus, your helper bot!\n
Working Modes:\n
1) Mirror Mode 🔄 — I reply to your messages with the same text
2) Reminder Mode ⏰ (in development) — Set reminders for important tasks
3) Other modes 🛠️ — coming soon...\n
Commands:\n
/start — Start the bot
/help — Show this help message
/mode — Switch between modes\n
Version: 0.2.2 | Developer: Milrus"""
        )
        await update.message.reply_text(help_text)
        logger.info(f'❓ Help requested by {update.effective_user.id}')

    except Exception as e:
        logger.error(f'❌ Error in help: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')
