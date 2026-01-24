import json
from datetime import datetime

def load_users():
    try:
        with open('data/users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_users(users_data):
    with open('data/users.json', 'w', encoding='utf-8') as f:
        json.dump(users_data, f, indent=4, ensure_ascii=False)

def update_user(user_id):
    users = load_users()
    curr_time = datetime.now()
    time_str = curr_time.strftime('%Y-%m-%d %H:%M:%S')
    user_id_str = str(user_id)
    if user_id_str not in users:
        users[user_id_str] = {
            'first_seen': time_str,
            'last_seen': time_str,
            'message_count': 1,
            'spam_flags': 0,
            'is_blocked': False,
            'ban_reason': None,
            'ban_date': None,
            'banned_by': None,
            'auto_banned': False
        }
    else:
        users[user_id_str]['last_seen'] = time_str
        curr_count = users[user_id_str].get('message_count', 0)
        users[user_id_str]['message_count'] = curr_count + 1

    save_users(users)

def increase_spam_flags(user_id):
    users = load_users()
    user_id_str = str(user_id)

    if user_id_str in users:
        curr_spam_flags = users[user_id_str].get('spam_flags', 0)
        users[user_id_str]['spam_flags'] = curr_spam_flags + 1
        save_users(users)
        return users
    
    return None