from utils.translations import texts
from utils.user_manager import load_users, save_users

def get_lang(user_id):
    users = load_users()
    return users.get(str(user_id), {}).get('language', 'ru')

def save_lang(user_id, new_lang):
    users = load_users()
    users[str(user_id)]['language']=new_lang
    save_users(users)

def get_reply_text(key, lang):
    if lang in texts:
        target_lang = lang
    else:
        target_lang = 'ru'
    return texts[target_lang].get(key)

def get_text_for_user(user_id, key):
    lang = get_lang(user_id)
    return get_reply_text(key, lang)
