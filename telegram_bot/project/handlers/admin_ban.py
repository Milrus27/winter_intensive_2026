import logging
from utils.user_manager import load_users
from utils.admin_check import is_admin
from config_loader import load_config
from utils.ban_manager import ban_user, is_user_banned

logger = logging.getLogger(__name__)

async def admin_ban(update, context):
    user_id = update.effective_user.id

    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_ban')
            await update.message.reply_text('🚫 No access')
            return

        if not context.args:
            await update.message.reply_text("❌ Specify the user's ID")
            return
        
        target_user_id_str = context.args[0]
        reason = ' '.join(context.args[1:]) if len(context.args) > 1 else ''

        try:
            target_user_id = int(target_user_id_str)

        except ValueError:
            await update.message.reply_text('❌ The ID must be a number')
            return
        
        if target_user_id <= 0:
            await update.message.reply_text('❌ Incorrect ID format')
            return

        users = load_users()
        
        if target_user_id == user_id:
            await update.message.reply_text('❌ You can not ban yourself')
            return
        
        config = load_config()
        admins = config.get('admin_ids', [])

        if target_user_id in admins:
            await update.message.reply_text('❌ You can not ban other admin')
            return
        
        if is_user_banned(target_user_id):
            await update.message.reply_text('❌ User is already banned')
            return

        success = ban_user(target_user_id, reason=reason, banned_by=user_id, auto=False)
        
        if success:
            logger.warning(f'✅ Admin {user_id} banned user {target_user_id} (reason: {reason})')
            response = f'✅ User {target_user_id} has been banned'
            if reason:
                response += f'\nReason: {reason}'
            await update.message.reply_text(response)
        else:
            await update.message.reply_text('❌ Failed to ban user')
    
    except Exception as e:
        logger.error(f'❌ Error in admin_ban: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')