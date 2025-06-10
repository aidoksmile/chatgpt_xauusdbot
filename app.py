from flask import Flask
from bot.telegram_bot import bot

app = Flask(__name__)

@app.route("/signal", methods=["GET"])
def get_signal():
    signal = bot.get_latest_signal()
    return signal

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
