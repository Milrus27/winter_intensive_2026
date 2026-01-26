from config_loader import save_config, load_config
from utils.user_manager import save_users, load_users
from datetime import datetime

def is_user_banned(user_id):
    config = load_config()
    users = load_users()

    blacklist = config.get('blacklist', [])
    is_in_blacklisted = False
    if user_id in blacklist:
        is_in_blacklisted = True
    
    is_blocked_in_db = False
    if str(user_id) in users:
        is_blocked_in_db = users[str(user_id)].get('is_blocked', False)
    
    return is_in_blacklisted or is_blocked_in_db

def ban_user(user_id, reason='', banned_by=None, auto=False):
    config = load_config()
    users = load_users()

    if is_user_banned(user_id):
        return False
    
    blacklist = config.get('blacklist', [])
    blacklist.append(user_id)
    config['blacklist'] = blacklist
    save_config(config)

    user_str = str(user_id)
    curr_time = datetime.now()
    time_str = curr_time.strftime('%Y-%m-%d %H:%M:%S')
    if user_str not in users:
        users[user_str] = {
            'first_seen': None,
            'last_seen': time_str,
            'message_count': 0,
            'spam_flags': 0,
            'is_blocked': True,
            'ban_reason': reason,
            'ban_date': time_str,
            'banned_by': banned_by,
            'auto_banned': auto
        }
    else:
        users[user_str]['is_blocked'] = True
        users[user_str]['ban_reason'] = reason
        users[user_str]['ban_date'] = time_str
        users[user_str]['banned_by'] = banned_by
        users[user_str]['auto_banned'] = auto

    save_users(users)
    return True

def unban_user(user_id):
    config = load_config()
    users = load_users()

    if not is_user_banned(user_id):
        return False
    
    blacklist = config.get('blacklist', [])
    if user_id in blacklist:
        blacklist.remove(user_id)
        config['blacklist'] = blacklist
        save_config(config)

    user_str = str(user_id)
    if user_str in users:
        users[user_str]['is_blocked'] = False
        users[user_str]['spam_flags'] = 0
        users[user_str]['ban_reason'] = None
        users[user_str]['ban_date'] = None
        users[user_str]['banned_by'] = None
        users[user_str]['auto_banned'] = False
        save_users(users)
    
    return True

def check_autoban(user_id, users_data=None):
    if users_data is None:
        users_data = load_users()

    user_id_str = str(user_id)

    if user_id_str in users_data:
        spam_flags = users_data[user_id_str].get('spam_flags', 0)
        is_blocked = users_data[user_id_str].get('is_blocked', False)

    if spam_flags >= 10 and not is_blocked:
        ban_user(user_id, reason='Autoban: more then 10 spam flags', auto=True)
        return True
    
    return False