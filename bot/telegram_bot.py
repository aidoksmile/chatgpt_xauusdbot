import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from strategy.entry_logic import generate_signal
from strategy.backtest import plot_backtest

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = "your_telegram_api_token_here"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Use /signal to get the latest signal.")

def get_signal(update: Update, context: CallbackContext) -> None:
    signal = generate_signal()  # Функция для получения сигнала
    update.message.reply_text(f"Latest Signal: {signal}")

def graph(update: Update, context: CallbackContext) -> None:
    graph_path = plot_backtest()  # График backtest
    update.message.reply_photo(photo=open(graph_path, "rb"))

def accuracy(update: Update, context: CallbackContext) -> None:
    accuracy = check_model_accuracy()  # Проверка точности модели
    update.message.reply_text(f"Model Accuracy: {accuracy}%")

def main():
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("signal", get_signal))
    dispatcher.add_handler(CommandHandler("graph", graph))
    dispatcher.add_handler(CommandHandler("accuracy", accuracy))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
