import os
import sys
from config_loader import load_config

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def is_admin(user_id):
    config = load_config()
    admin_ids = config.get('admin_ids', [])
    return user_id in admin_ids
