import logging
from config_loader import load_config
from utils.admin_check import is_admin
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def admin_help(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_help')
            await update.message.reply_text(get_text_for_user(user_id, 'admin_command_used_by_user'))
            return
        
        logger.info(f'✅ Admin {user_id} called /admin_help')

        data = load_config()
        admin_list = data.get('admin_ids', [])
        admins = len(admin_list)

        message = ''.join([get_text_for_user(user_id, 'admin_help_commands'),
                           get_text_for_user(user_id, 'admin_help_admins').format(admins=admins),
                           get_text_for_user(user_id, 'admin_help_admin_id').format(user_id=user_id),
                           get_text_for_user(user_id, 'admin_help_note')])
        
        await update.message.reply_text(message)

    except Exception as e:
        logger.error(f'❌ Error in admin_help: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))