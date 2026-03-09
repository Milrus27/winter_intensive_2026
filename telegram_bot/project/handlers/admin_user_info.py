import logging
from utils.user_manager import load_users
from utils.admin_check import is_admin
from config_loader import load_config
from utils.user_manager import update_user
from utils.language import get_text_for_user

logger = logging.getLogger(__name__)

async def admin_user_info(update, context):
    user_id = update.effective_user.id
    update_user(user_id)
    try:
        if not is_admin(user_id):
            logger.warning(f'🚫 Non-admin user {user_id} tried to access /admin_user_info')
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

        users = load_users()

        if target_user_id_str not in users:
            await update.message.reply_text(get_text_for_user(user_id, 'admin_user_info_not_found'))
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
            name_display = ' '.join(name_parts) if name_parts else get_text_for_user(user_id, 'admin_user_info_name_not_available')
            username_display = f"@{telegram_info['username']}" if telegram_info['username'] else get_text_for_user(user_id, 'admin_user_info_username_not_set')
        else:
            name_display = get_text_for_user(user_id, 'admin_user_info_telegram_unavailable')
            username_display = get_text_for_user(user_id, 'admin_user_info_telegram_unavailable')

        message = []

        message.append(get_text_for_user(user_id, 'admin_user_info_header').format(target_user_id=target_user_id))

        message.append(get_text_for_user(user_id, 'admin_user_info_name').format(name_display=name_display))
        message.append(get_text_for_user(user_id, 'admin_user_info_username').format(username_display=username_display))

        message.append('')

        message.append(get_text_for_user(user_id, 'admin_user_info_first_seen').format(first_seen=first_seen))
        message.append(get_text_for_user(user_id, 'admin_user_info_last_seen').format(last_seen=last_seen))
        message.append(get_text_for_user(user_id, 'admin_user_info_messages').format(message_count=message_count))
        message.append(get_text_for_user(user_id, 'admin_user_info_spam_flags').format(spam_flags=spam_flags))

        message.append('')

        banned_status = get_text_for_user(user_id, 'admin_user_info_banned_yes') if is_in_blacklist else get_text_for_user(user_id, 'admin_user_info_banned_no')
        message.append(get_text_for_user(user_id, 'admin_user_info_blocking_status').format(banned_status=banned_status))

        if ban_reason:
            message.append(get_text_for_user(user_id, 'admin_user_info_ban_reason').format(reason=ban_reason))
        if ban_date:
            message.append(get_text_for_user(user_id, 'admin_user_info_ban_date').format(date=ban_date))
        if banned_by:
            message.append(get_text_for_user(user_id, 'admin_user_info_banned_by').format(banned_by=banned_by))
        if auto:
            message.append(get_text_for_user(user_id, 'admin_user_info_auto_banned'))

        final_message = '\n'.join(message)
        await update.message.reply_text(final_message)

    except Exception as e:
        logger.error(f'❌ Error in admin_user_info: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))