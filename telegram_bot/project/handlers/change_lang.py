import logging
from datetime import datetime
from utils.user_manager import update_user, load_users
from utils.language import save_lang, get_text_for_user

logger = logging.getLogger(__name__)

async def change_lang(update, context):
    user_id = update.effective_user.id
    user_id_str = str(user_id)
    update_user(user_id)
    try:
        users = load_users()

        if not context.args:
            await update.message.reply_text(get_text_for_user(user_id, 'lang_no_args'))
            return
        
        new_language = context.args[0].lower().strip()

        if new_language not in ['en', 'ru']:
            await update.message.reply_text(get_text_for_user(user_id, 'incorrect_lang'))
            return
        
        save_lang(user_id, new_language)

        logging.info(f'📝 The user {user_id} changed language')
        await update.message.reply_text(get_text_for_user(user_id, 'language_changed'))
        
    except Exception as e:
        logger.error(f'❌ Error in lang: {e}')
        await update.message.reply_text(get_text_for_user(user_id, 'error'))