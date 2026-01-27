import logging
from utils.admin_check import is_admin

logger = logging.getLogger(__name__)

async def help_command(update, context):
    user_id = update.effective_user.id
    try:
        help_text = (
            """I'm Milrus, your helper bot! 🤖\n
Bot Features:\n
✅ Mirror Mode 🔄 — I reply to your messages with the same text
✅ Reminder Mode ⏰ — Set reminders for important tasks
✅ Admin Panel 🛡️ — User management for administrators\n
Commands:\n
/start — Start the bot
/help — Show this help message
/mode — Show current bot configuration
/remind [text] [hours] — Create a reminder (1-168 hours)
/my_reminds — List your reminders (max 5)
/remove_remind [ID] — Delete a reminder by ID\n
📌 All features work simultaneously in hybrid mode.\n
Version: 0.6.1 | Developer: Milrus"""
        )
        await update.message.reply_text(help_text)
        logger.info(f'❓ Help requested by {user_id}')

        if is_admin(user_id):
            logger.info(f'💡 Admin {user_id} received admin hint in /help')
            await update.message.reply_text('💡 You are an admin. Use /admin_help for a list of commands')
    except Exception as e:
        logger.error(f'❌ Error in help: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')