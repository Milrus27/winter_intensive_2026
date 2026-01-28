import json
from datetime import datetime, timedelta, timezone

def load_reminders():
    try:
        with open('data/reminders.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_reminders(reminders_data):
    with open('data/reminders.json', 'w', encoding='utf-8') as f:
        json.dump(reminders_data, f, indent=4, ensure_ascii=False)

def add_reminder(user_id, text, hours):
    reminders = load_reminders()
    user_id_str = str(user_id)

    if user_id_str not in reminders:
        reminders[user_id_str] = []

    if len(reminders[user_id_str]) >= 5:
        return None
    
    reminder_id = int(datetime.now().timestamp())

    next_time = datetime.now(timezone.utc) + timedelta(hours=hours)
    new_reminder = {
        'id': reminder_id,
        'text': text,
        'hours': hours,
        'next_run': next_time.isoformat()
    }

    reminders[user_id_str].append(new_reminder)
    save_reminders(reminders)
    return reminder_id

def get_user_reminders(user_id):
    reminders = load_reminders()
    user_id_str = str(user_id)

    user_reminders = reminders.get(user_id_str, [])
    return user_reminders

def remove_reminder(user_id, reminder_id):
    reminders = load_reminders()
    user_id_str = str(user_id)

    if user_id_str not in reminders:
        return False
    
    for remind in reminders[user_id_str]:
        if remind['id'] == reminder_id:
            reminders[user_id_str].remove(remind)
            save_reminders(reminders)
            return True
    
    return False