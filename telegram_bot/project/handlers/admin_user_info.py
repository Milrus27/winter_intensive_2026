import logging
from config_loader import load_config
from utils.admin_check import is_admin

logger = logging.getLogger(__name__)

async def admin_user_info(update, context):
    user_id = update.effective_user.id

    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_user_info')
            await update.message.reply_text('🚫 No access')
            return
        
        logger.info(f'✅ Admin {user_id} called /admin_user_info')

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

    except Exception as e:
        logger.error(f'❌ Error in admin_user_info: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')