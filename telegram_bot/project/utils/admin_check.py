from config_loader import load_config

def is_admin(user_id):
    config = load_config()
    admin_ids = config.get('admin_ids', [])
    return user_id in admin_ids
