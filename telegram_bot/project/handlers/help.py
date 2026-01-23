import logging
from utils.admin_check import is_admin

logger = logging.getLogger(__name__)

async def help_command(update, context):
    user_id = update.effective_user.id
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
Version: 0.4.0 | Developer: Milrus"""
        )
        await update.message.reply_text(help_text)
        logger.info(f'❓ Help requested by {user_id}')

        if is_admin(user_id):
            logger.info(f'💡 Admin {user_id} recieved admin hint in /help')
            await update.message.reply_text('💡 You are an admin. Use /admin_help for a list of commands')
    except Exception as e:
        logger.error(f'❌ Error in help: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')
