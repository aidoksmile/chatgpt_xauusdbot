# Модуль backtesting
import matplotlib.pyplot as plt

def plot_backtest():
    # Пример генерации графика
    equity_curve = [1000, 1050, 1020, 1100]
    plt.plot(equity_curve)
    plt.savefig("equity_curve.png")
    return "equity_curve.png"
