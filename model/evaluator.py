# Оценка точности модели
def evaluate_model(model, data):
    loss, accuracy = model.evaluate(data, data)
    return accuracy
