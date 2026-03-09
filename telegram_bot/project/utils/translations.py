texts = {
    'en': {
    'error': '❌ Sorry, something went wrong. Please try again later.',
    'language_changed': '✅ Language changed to English',
    'start': '''👋 Hello, {user_name}! I'm Milrus — your reminder bot.

📝 I can help you create reminders that will be sent once after a set number of hours.
⏰ Currently, reminders are sent once and then deleted (no repeats).
✨ Use /help to see all commands.

🔧 Version: 1.1.0''',
    'start_again': 'Welcome back, {user_name}! :)',
    'help': '''I'm Milrus, your assistant bot! 🤖

Bot features:
✅ Mirror Mode 🔄 — I reply to your messages with the same text.
✅ Reminder Mode ⏰ — Set reminders for important tasks.
✅ Admin Panel 🛡️ — User management for administrators.

Commands:
/start — Start the bot
/help — Show this help message
/lang [en/ru] — Change language
/mode — Show current bot configuration
/remind [text] [hours] — Create a reminder (1-168 hours)
/reminders — List your reminders (max 5)
/remove_remind [ID] — Delete a reminder by ID

📌 All features work simultaneously in hybrid mode.
⚠️ Reminders may be delayed by up to 5 minutes (maximum).

Version: 1.1.0 | Developer: Milrus''',
    'help_admin_hint': '💡 You are an admin. Use /admin_help for the list of admin commands.',
    'lang_no_args': '❌ Usage:\n/lang en\n/lang ru',
    'incorrect_lang': '❌ Invalid language. Choose en or ru.',
    'echo_banned_user': '''🚫 You have been banned for spamming in mirror mode.
📝 You can still use: /remind, /reminders, /remove_remind
🔄 Contact an administrator to get unbanned.''',
    'echo_not_user_text': '📝 Please type something.',
    'echo_invalid_len': '❌ Message too long (maximum 1000 characters).',
    'echo_invalid_chars': '❌ Message contains invalid characters.',
    'echo_limit': '⏳ Please slow down.',
    'echo_ban_spam': '🚫 You have been banned for spam.',
    'mode': '''🎭 Current mode: HYBRID (all features active)

✅ Mirror Mode: Always ON
✅ Reminder Mode: Always ON
✅ Admin Panel: Available to admins

⚙️ All features work simultaneously.''',
    'remind_no_context_args': '❌ Usage: /remind [text] [hours]',
    'remind_incorrect_hours': '❌ Hours must be a whole number between 1 and 168.',
    'remind_no_hours': '❌ Please specify the number of hours.',
    'remind_incorrect_range': '❌ The time must be between 1 and 168 hours.',
    'remind_no_text': '❌ Please enter the reminder text.',
    'remind_incorrect_len': '❌ Reminder text is too long (maximum 1000 characters).',
    'reminder_added': '✅ Reminder added!\nID: {reminder_id}',
    'reminders_limit': '❌ You have reached the limit of 5 reminders. Delete one to add a new one.',
    'no_reminders': '📭 You don\'t have any reminders yet.',
    'reminders_message(count)': '📝 Your reminders ({reminders_count}/5):',
    'reminder_block_id': '🔔 ID: <code>{reminder_id}</code>',
    'reminder_block_text': '📝 Text: {reminder_text}',
    'reminder_block_hours': '⏰ Will be sent in: {reminder_time} hour{hours_eng}',
    'reminder_block_due': '🕐 Due (UTC): {reminder_next_run}',
    'reminder_block_help': '\n❓ To delete a reminder, send /remove_remind [ID]\n💡 Tap the ID to copy it.',
    'remove_reminder_no_context_args': '❌ Usage: /remove_remind [ID]\n📋 View IDs: /reminders\n⏰ Create a reminder: /remind [text] [hours]',
    'remove_reminder_id_error': '❌ The ID must be a number.',
    'remove_reminder_success': '✅ Reminder {reminder_id} has been deleted.',
    'remove_reminder_fail': '❌ No reminder found with ID {reminder_id}.',
    'admin_command_used_by_user': '🚫 Access denied.',
    'admin_ban_no_context_args': '❌ Please specify the user ID.',
    'admin_ban_incorrect_id_number': '❌ The ID must be a number.',
    'admin_ban_negative_id': '❌ Invalid ID format.',
    'admin_ban_myself': '❌ You cannot ban yourself.',
    'admin_ban_admin': '❌ You cannot ban another admin.',
    'admin_ban_banned_user': '❌ User is already banned.',
    'admin_ban_success': '✅ User {target_user_id} has been banned.',
    'admin_ban_reason': '\n📋 Reason: {reason}',
    'admin_ban_fail': '❌ Failed to ban user.',
    'admin_help_commands': '''🛡️ Admin Panel

Available commands:
/admin_stats — Bot statistics
/admin_user_info [ID] — User information
/admin_ban [ID] [reason] — Ban a user
/admin_unban [ID] — Unban a user
/admin_help — This help page

System information:\n''',
    'admin_help_admins': '👑 Total admins: {admins}\n',
    'admin_help_admin_id': '🆔 Your ID: {user_id}\n',
    'admin_help_note': '📊 Use these commands with caution.',
    'admin_unban_unbanned_user': '❌ User is already unbanned.',
    'admin_unban_success': '✅ User {target_user_id} has been unbanned.',
    'admin_unban_fail': '❌ User is not banned.',
    'admin_stats_text': '📊 Bot statistics:\n',
    'admin_stats_users': '👥 Total users: {total_users}\n',
    'admin_stats_messages': '💬 Total messages: {total_messages}\n',
    'admin_stats_active': '🔥 Active users: {total_active_users}\n',
    'admin_stats_total_banned': '🚫 Total banned: {total_banned}\n',
    'admin_stats_manual_banned': '👨‍💻 Manually banned: {manual_banned}\n',
    'admin_stats_auto_banned': '🤖 Auto‑banned: {auto_banned}\n',
    'admin_stats_log_size': '📁 Log size: {log_size} bytes',
    'admin_user_info_not_found': '❌ User not found.',
    'admin_user_info_name_not_available': 'Name not available',
    'admin_user_info_username_not_set': 'Username not set',
    'admin_user_info_telegram_unavailable': 'Telegram information unavailable',
    'admin_user_info_header': '👤 User {target_user_id}',
    'admin_user_info_name': '👨‍💼 Name: {name_display}',
    'admin_user_info_username': '📱 Username: {username_display}',
    'admin_user_info_first_seen': '📅 First message: {first_seen}',
    'admin_user_info_last_seen': '⏰ Last message: {last_seen}',
    'admin_user_info_messages': '💬 Messages: {message_count}',
    'admin_user_info_spam_flags': '🚨 Spam flags: {spam_flags}',
    'admin_user_info_blocking_status': '\nBlocking status:\nBanned (mirror mode only): {banned_status}',
    'admin_user_info_banned_yes': '🔴 Yes',
    'admin_user_info_banned_no': '🟢 No',
    'admin_user_info_ban_reason': '\n📋 Ban reason: {reason}',
    'admin_user_info_ban_date': '\n🗓️ Ban date: {date}',
    'admin_user_info_banned_by': '\n👨‍💼 Banned by: {banned_by}',
    'admin_user_info_auto_banned': '\n🤖 Auto‑banned'},


    'ru': {
    'error': '❌ Что-то пошло не так. Попробуйте позже.',
    'language_changed': '✅ Язык изменён на русский',
    'start': '''👋 Привет, {user_name}! Я Милрус — бот-напоминалка.

📝 Я помогу вам создать напоминание, которое придёт через нужное количество часов.
⏰ Сейчас напоминания отправляются один раз, а потом удаляются (без повторов).
✨ Список всех команд — /help.

🔧 Версия: 1.1.0''',
    'start_again': 'С возвращением, {user_name}! :)',
    'help': '''Я Милрус, ваш помощник! 🤖

Возможности бота:
✅ Режим зеркала 🔄 — я отвечаю на ваши сообщения тем же текстом.
✅ Режим напоминаний ⏰ — напоминания о важных делах.
✅ Панель администратора 🛡️ — управление пользователями для админов.

Команды:
/start — запустить бота
/help — показать эту справку
/lang [en/ru] — сменить язык
/mode — показать текущие настройки бота
/remind [текст] [часы] — создать напоминание (от 1 до 168 часов)
/reminders — список ваших напоминаний (максимум 5)
/remove_remind [ID] — удалить напоминание по ID

📌 Все режимы работают одновременно.
⚠️ Напоминания могут задержаться максимум на 5 минут.

Версия: 1.1.0 | Разработчик: Milrus''',
    'help_admin_hint': '💡 Вы администратор. Список команд для админов — /admin_help',
    'lang_no_args': '❌ Укажите язык:\n/lang en\n/lang ru',
    'incorrect_lang': '❌ Неверный язык. Выберите en или ru',
    'echo_banned_user': '''🚫 Вас заблокировали за спам в режиме зеркала.
📝 Вы всё ещё можете использовать: /remind, /reminders, /remove_remind
🔄 Чтобы восстановить доступ, свяжитесь с администратором.''',
    'echo_not_user_text': '📝 Напишите что-нибудь',
    'echo_invalid_len': '❌ Сообщение слишком длинное (максимум 1000 символов)',
    'echo_invalid_chars': '❌ Сообщение содержит недопустимые символы',
    'echo_limit': '⏳ Пожалуйста, не так быстро',
    'echo_ban_spam': '🚫 Вы заблокированы за спам',
    'mode': '''🎭 Текущий режим: ГИБРИДНЫЙ (все функции активны)

✅ Режим зеркала: всегда включён
✅ Режим напоминаний: всегда включён
✅ Панель администратора: доступна админам

⚙️ Все функции работают одновременно.''',
    'remind_no_context_args': '❌ Использование: /remind [текст] [часы]',
    'remind_incorrect_hours': '❌ Количество часов должно быть целым числом от 1 до 168',
    'remind_no_hours': '❌ Укажите количество часов',
    'remind_incorrect_range': '❌ Время должно быть от 1 до 168 часов',
    'remind_no_text': '❌ Введите текст напоминания',
    'remind_incorrect_len': '❌ Текст слишком длинный (максимум 1000 символов)',
    'reminder_added': '✅ Напоминание добавлено!\nID: {reminder_id}',
    'reminders_limit': '❌ Лимит напоминаний — 5. Удалите одно, чтобы добавить новое',
    'no_reminders': '📭 У вас пока нет напоминаний',
    'reminders_message(count)': '📝 Ваши напоминания ({reminders_count}/5):',
    'reminder_block_id': '🔔 ID: <code>{reminder_id}</code>',
    'reminder_block_text': '📝 Текст: {reminder_text}',
    'reminder_block_hours': '⏰ Будет отправлено через: {reminder_time} {hours_rus}',
    'reminder_block_due': '🕐 Время отправки (UTC): {reminder_next_run}',
    'reminder_block_help': '\n❓ Чтобы удалить напоминание, отправьте /remove_remind [ID]\n💡 Нажмите на ID, чтобы скопировать',
    'remove_reminder_no_context_args': '❌ Использование: /remove_remind [ID]\n📋 Список ID — /reminders\n⏰ Создать напоминание — /remind [текст] [часы]',
    'remove_reminder_id_error': '❌ ID должен быть числом',
    'remove_reminder_success': '✅ Напоминание {reminder_id} удалено',
    'remove_reminder_fail': '❌ Напоминание с ID {reminder_id} не найдено',
    'admin_command_used_by_user': '🚫 Доступ запрещён',
    'admin_ban_no_context_args': '❌ Укажите ID пользователя',
    'admin_ban_incorrect_id_number': '❌ ID должен быть числом',
    'admin_ban_negative_id': '❌ Неверный формат ID',
    'admin_ban_myself': '❌ Нельзя забанить самого себя',
    'admin_ban_admin': '❌ Нельзя забанить другого администратора',
    'admin_ban_banned_user': '❌ Пользователь уже забанен',
    'admin_ban_success': '✅ Пользователь {target_user_id} заблокирован',
    'admin_ban_reason': '\n📋 Причина: {reason}',
    'admin_ban_fail': '❌ Не удалось заблокировать пользователя',
    'admin_help_commands': '''🛡️ Панель администратора

Доступные команды:
/admin_stats — статистика бота
/admin_user_info [ID] — информация о пользователе
/admin_ban [ID] [причина] — заблокировать пользователя
/admin_unban [ID] — разблокировать пользователя
/admin_help — эта справка

Информация о системе:\n''',
    'admin_help_admins': '👑 Всего администраторов: {admins}\n',
    'admin_help_admin_id': '🆔 Ваш ID: {user_id}\n',
    'admin_help_note': '📊 Используйте эти команды осторожно',
    'admin_unban_unbanned_user': '❌ Пользователь уже разблокирован',
    'admin_unban_success': '✅ Пользователь {target_user_id} разблокирован',
    'admin_unban_fail': '❌ Пользователь не заблокирован',
    'admin_stats_text': '📊 Статистика бота:\n',
    'admin_stats_users': '👥 Всего пользователей: {total_users}\n',
    'admin_stats_messages': '💬 Всего сообщений: {total_messages}\n',
    'admin_stats_active': '🔥 Активных пользователей: {total_active_users}\n',
    'admin_stats_total_banned': '🚫 Всего заблокировано: {total_banned}\n',
    'admin_stats_manual_banned': '👨‍💻 Заблокировано админами: {manual_banned}\n',
    'admin_stats_auto_banned': '🤖 Заблокировано автоматически: {auto_banned}\n',
    'admin_stats_log_size': '📁 Размер логов: {log_size} байт',
    'admin_user_info_not_found': '❌ Пользователь не найден',
    'admin_user_info_name_not_available': 'Имя недоступно',
    'admin_user_info_username_not_set': 'Имя пользователя не указано',
    'admin_user_info_telegram_unavailable': 'Информация Telegram недоступна',
    'admin_user_info_header': '👤 Пользователь {target_user_id}',
    'admin_user_info_name': '👨‍💼 Имя: {name_display}',
    'admin_user_info_username': '📱 Username: {username_display}',
    'admin_user_info_first_seen': '📅 Дата первого сообщения: {first_seen}',
    'admin_user_info_last_seen': '⏰ Дата последнего сообщения: {last_seen}',
    'admin_user_info_messages': '💬 Всего сообщений: {message_count}',
    'admin_user_info_spam_flags': '🚨 Флагов спама: {spam_flags}',
    'admin_user_info_blocking_status': '\nСтатус блокировки:\nЗабанен (только режим зеркала): {banned_status}',
    'admin_user_info_banned_yes': '🔴 Да',
    'admin_user_info_banned_no': '🟢 Нет',
    'admin_user_info_ban_reason': '\n📋 Причина бана: {reason}',
    'admin_user_info_ban_date': '\n🗓️ Дата бана: {date}',
    'admin_user_info_banned_by': '\n👨‍💼 Заблокировал администратор: {banned_by}',
    'admin_user_info_auto_banned': '\n🤖 Заблокировано автоматически'}
}