import os
import logging
from config_loader import load_config
from utils.user_manager import load_users
from utils.admin_check import is_admin
from datetime import datetime
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def admin_stats(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_stats')
            await update.message.reply_text(get_text_for_user(user_id, 'admin_command_used_by_user'))
            return

        logger.info(f'✅ Admin {user_id} called /admin_stats')

        users = load_users()

        total_users = len(users)

        total_active_users = 0
        for user_data in users.values():
            if user_data.get('first_seen') is not None:
                total_active_users += 1

        total_messages = 0
        for user_data in users.values():
            total_messages += user_data.get('message_count', 0)

        curr_time = datetime.now()
        today = curr_time.strftime('%Y-%m-%d')

        total_banned = 0
        manual_banned = 0
        auto_banned = 0
        for user_data in users.values():
            if user_data.get('is_blocked', False):
                total_banned += 1
                if user_data.get('auto_banned'):
                    auto_banned += 1
                else:
                    manual_banned += 1

        log_size = 0
        if os.path.exists('logs/bot.log'):
            log_size = os.path.getsize('logs/bot.log')

        message = ''.join([get_text_for_user(user_id, 'admin_stats_text'),
                           get_text_for_user(user_id, 'admin_stats_users').format(total_users=total_users),
                           get_text_for_user(user_id, 'admin_stats_messages').format(total_messages=total_messages),
                           get_text_for_user(user_id, 'admin_stats_active').format(total_active_users=total_active_users),
                           get_text_for_user(user_id, 'admin_stats_total_banned').format(total_banned=total_banned),
                           get_text_for_user(user_id, 'admin_stats_manual_banned').format(manual_banned=manual_banned),
                           get_text_for_user(user_id, 'admin_stats_auto_banned').format(auto_banned=auto_banned),
                           get_text_for_user(user_id, 'admin_stats_log_size').format(log_size=log_size)])
        
        await update.message.reply_text(message)

    except Exception as e:
        logger.error(f'❌ Error in admin_stats: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))