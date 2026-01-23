import logging
from config_loader import load_config
from utils.admin_check import is_admin

logger = logging.getLogger(__name__)

async def admin_help(update, context):
    user_id = update.effective_user.id

    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_help')
            await update.message.reply_text('🚫 No access')
            return
        
        logger.info(f'✅ Admin {user_id} called /admin_help')

        data = load_config()
        admin_list = data.get('admin_ids', [])
        admins = len(admin_list)

        message = F'''🛡️ Bot Admin Panel\n
Available Commands:\n
/admin_stats - Bot statistics
/admin_user_info <ID> - User information.
/admin_ban <ID> [reason] - Ban a user
/admin_unban <ID> - Unban
/admin_help - This help page\n
System Information:
👑 Total admins: {admins}
🆔 Your ID: {user_id}\n
📊 Use this commands with caution'''
        
        await update.message.reply_text(message)

    except Exception as e:
        logger.error(f'❌ Error in admin_help: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')