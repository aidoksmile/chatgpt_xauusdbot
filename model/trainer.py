# Функция для обучения модели
from sklearn.model_selection import TimeSeriesSplit
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_model(data):
    model = Sequential()
    model.add(Dense(64, input_dim=data.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # TimeSeriesSplit для обучения
    tscv = TimeSeriesSplit(n_splits=5)
    for train_index, test_index in tscv.split(data):
        X_train, X_test = data.iloc[train_index], data.iloc[test_index]
        model.fit(X_train, X_test, epochs=10, batch_size=32)

    return model
