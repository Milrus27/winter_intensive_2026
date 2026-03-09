import logging
from config_loader import load_config
from utils.user_manager import load_users
from utils.admin_check import is_admin
from config_loader import load_config
from utils.ban_manager import unban_user, is_user_banned
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def admin_unban(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_unban')
            await update.message.reply_text(get_text_for_user(user_id, 'admin_command_used_by_user'))
            return

        if not context.args:
            await update.message.reply_text(get_text_for_user(user_id, 'admin_ban_no_context_args'))
            return
        
        target_user_id_str = context.args[0]

        try:
            target_user_id = int(target_user_id_str)

        except ValueError:
            await update.message.reply_text(get_text_for_user(user_id, 'admin_ban_incorrect_id_number'))
            return
        
        if target_user_id <= 0:
            await update.message.reply_text(get_text_for_user(user_id, 'admin_ban_negative_id'))
            return
        
        if not is_user_banned(target_user_id):
            await update.message.reply_text(get_text_for_user(user_id, 'admin_unban_unbanned_user'))
            return

        success = unban_user(target_user_id)

        if success:
            logger.warning(f'✅ Admin {user_id} unbanned user {target_user_id}')
            await update.message.reply_text(get_text_for_user(user_id, 'admin_unban_success').format(target_user_id=target_user_id))
        else:
            await update.message.reply_text(get_text_for_user(user_id, 'admin_unban_fail'))
    
    except Exception as e:
        logger.error(f'❌ Error in admin_unban: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))