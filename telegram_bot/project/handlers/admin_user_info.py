import logging
from utils.user_manager import load_users
from utils.admin_check import is_admin
from config_loader import load_config
from utils.user_manager import update_user

logger = logging.getLogger(__name__)

async def admin_user_info(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_user_info')
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

        users = load_users()

        if target_user_id_str not in users:
            await update.message.reply_text('❌ The user was not found')
            return
        
        user_data = users[target_user_id_str]

        try:
            chat = await context.bot.get_chat(target_user_id)

            first_name = chat.first_name
            last_name = chat.last_name
            username = chat.username

            telegram_info = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username
            }
        
        except Exception as e:
            logger.warning(f'❌ Could not get telegram info for user {target_user_id}: {e}')
            telegram_info = None

        first_seen = user_data.get('first_seen', 'unknown')
        last_seen = user_data.get('last_seen', 'unknown')
        message_count = user_data.get('message_count', 0)
        spam_flags = user_data.get('spam_flags', 0)
        is_blocked = user_data.get('is_blocked', False)

        config = load_config()
        
        blacklist = config.get('blacklist', [])

        ban_reason = user_data.get('ban_reason', None)
        ban_date = user_data.get('ban_date', None)

        is_in_blacklist = False
        for user_id_in_list in blacklist:
            if str(user_id_in_list) == target_user_id_str:
                is_in_blacklist = True
                break
        
        banned_by = user_data.get('banned_by')
        auto = user_data.get('auto_banned', False)

        logger.info(f'✅ Admin {user_id} called /admin_user_info about {target_user_id}')

        if telegram_info:
            name_parts = []
            if telegram_info['first_name']:
                name_parts.append(telegram_info['first_name'])
            if telegram_info['last_name']:
                name_parts.append(telegram_info['last_name'])
        
            name_display = ' '.join(name_parts) if name_parts else 'Name not available'

            if telegram_info['username']:
                username_display = f"@{telegram_info['username']}"
            else:
                username_display = 'Username not set'
        else:
            name_display = 'Telegram information not available'
            username_display = 'Telegram information not available'

        message = f'''👤 The user {target_user_id}

👨‍💼 Name: {name_display}
📱 Username: {username_display}

📅 First message date: {first_seen}
⏰ Last message date: {last_seen}
💬 Total messages: {message_count}
🚨 Spam flags: {spam_flags}

Blocking status:
Banned (only echo mode can be banned): {'🔴 Yes 🔴' if is_in_blacklist else '🟢 No 🟢'}'''

        if ban_reason:
            message += f'\n📋 Ban reason: {ban_reason}'
        if ban_date:
            message += f'\n🗓️ Ban date: {ban_date}'
        if banned_by:
            message += f'\n👨‍💼 Banned by admin: {banned_by}'
        if auto:
            message += '\n🤖 Banned automatically by system'

        await update.message.reply_text(message)

    except Exception as e:
        logger.error(f'❌ Error in admin_user_info: {e}')
        await update.message.reply_text('❌ Sorry, something went wrong:(')