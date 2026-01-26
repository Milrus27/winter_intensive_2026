import logging
from config_loader import load_config
from utils.user_manager import load_users
from utils.admin_check import is_admin
from config_loader import load_config
from utils.ban_manager import unban_user, is_user_banned

logger = logging.getLogger(__name__)

async def admin_unban(update, context):
    user_id = update.effective_user.id

    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_unban')
            await update.message.reply_text('🚫 No access')
            return

        if not context.args:
            await update.message.reply_text("❌ Specify the user's ID")
            return
        
        target_user_id_str = context.args[0]

        try:
            target_user_id = int(target_user_id_str)

        except ValueError:
            await update.message.reply_text('❌ The ID must be a number')
            return
        
        if target_user_id <= 0:
            await update.message.reply_text('❌ Incorrect ID format')
            return
        
        if not is_user_banned(target_user_id):
            await update.message.reply_text('❌ User is already unbanned')
            return

        success = unban_user(target_user_id)

        if success:
            users = load_config()
            logger.warning(f'✅ Admin {user_id} unbanned user {target_user_id}')
            await update.message.reply_text(f'✅ User {target_user_id} has been unbanned')
        else:
            await update.message.reply_text('❌ User is not banned')
    
    except Exception as e:
        logger.error(f'❌ Error in admin_unban: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')