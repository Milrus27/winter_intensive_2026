texts = {
    'en': {'language_changed': '✅ You changed the language to English',
           'start': """👋 Hello, {user_name}! I'm Milrus Reminder Bot!\n
📝 I can help you create reminders that will send once after X hours
⏰ Currently, reminders are sent once and then deleted (not repeated)
✨ Use /help to see all commands\n
🔧 Version: pre 1.1.0""",
           'start_again': 'Hello again, {user_name}:)',
           'help': """I'm Milrus, your helper bot! 🤖\n
Bot Features:\n
✅ Mirror Mode 🔄 — I reply to your messages with the same text
✅ Reminder Mode ⏰ — Set reminders for important tasks
✅ Admin Panel 🛡️ — User management for administrators\n
Commands:\n
/start — Start the bot
/help — Show this help message
/lang [en/ru] — change language
/mode — Show current bot configuration
/remind [text] [hours] — Create a reminder (1-168 hours)
/reminders — List your reminders (max 5)
/remove_remind [ID] — Delete a reminder by ID\n
📌 All features work simultaneously in hybrid mode\n
Note: your reminders can be delayed by a maximum of 5 minutes (but this is the maximum limit)\n
Version: pre 1.1.0 | Developer: Milrus"""},

    'ru': {'language_changed': '✅ Вы изменили язык на русский',
           'start': """👋 Привет, {user_name}! Я бот-напоминалка Милрус!\n
📝 Я могу помочь вам создать напоминания, которые будут отправляться один раз через X часов
⏰ В настоящее время напоминания отправляются один раз, а затем удаляются (не повторяются)
✨ Используйте /help, чтобы увидеть все команды\n
🔧 Версия: pre 1.1.0""",
           'start_again': 'Привет снова, {user_name}:)',
           'help': """Я Милрус, ваш бот-помощник! 🤖\n
Функции бота:\n
✅ Режим зеркала 🔄 — Я отвечаю на ваши сообщения тем же текстом
✅ Режим напоминаний ⏰ — Устанавливайте напоминания о важных задачах
✅ Панель администратора 🛡️ — Управление пользователями для администраторов\n
Команды:\n
/start — Запустить бота
/help — Показать справку (это сообщение)
/lang [en/ru] — Изменить язык
/mode — Показать текущую конфигурацию бота
/remind [text] [hours] — Создать напоминание (1-168 часов)
/reminders — Список ваших напоминаний (максимум 5)
/remove_remind [ID] — Удалить напоминание по ID\n
📌 Все функции работают одновременно в гибридном режиме\n
Примечание: ваши напоминания могут быть отложены максимум на 5 минут (но это максимальное ограничение)\n
Версия: pre 1.1.0 | Разработчик: Milrus"""}
}