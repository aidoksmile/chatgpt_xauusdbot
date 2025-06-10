# Логика отправки уведомлений в Telegram
def send_telegram_message(message):
    from telegram import Bot
    bot = Bot(token="your_telegram_api_token_here")
    bot.send_message(chat_id="your_chat_id", text=message)
