# Планировщик для проверки рынка каждые 15 минут
import time
from bot.notifier import send_telegram_message
from data.fetcher import fetch_data
from model.trainer import train_model
from model.evaluator import evaluate_model

def start_scheduler():
    while True:
        data = fetch_data("XAUUSD=X", interval="15m")
        if data is not None:
            model = train_model(data)
            accuracy = evaluate_model(model, data)
            if accuracy < 0.8:
                model = train_model(data)  # Автопереобучение
            send_telegram_message("New signal!")
        time.sleep(900)  # 15 минут
