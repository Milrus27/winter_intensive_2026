import os
import logging
from config_loader import load_config
from utils.user_manager import load_users
from utils.admin_check import is_admin
from datetime import datetime

logger = logging.getLogger(__name__)

async def admin_stats(update, context):
    user_id = update.effective_user.id

    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_stats')
            await update.message.reply_text('🚫 No access')
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

        message = f'''
    📊 Bot statistics:

👥 Total users: {total_users}
💬 Total messages: {total_messages}
🔥 Total active users: {total_active_users}
🚫 Total banned: {total_banned}
👨‍💻 Manual banned: {manual_banned}
🤖 Auto banned: {auto_banned}
📁 Log size: {log_size} bytes'''
        
        await update.message.reply_text(message)

    except Exception as e:
        logger.error(f'❌ Error in admin_stats: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')