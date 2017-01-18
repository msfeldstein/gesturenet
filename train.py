from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

class Trainer:
    def __init__(self, listener):
        self.listener = listener
        self.data_dim = 2
        self.timesteps = 8
        self.nb_classes = 5

        # expected input data shape: (batch_size, timesteps, data_dim)
        self.model = Sequential()
        self.model.add(LSTM(32, return_sequences=True,
                       input_shape=(self.timesteps, self.data_dim)))  # returns a sequence of vectors of dimension 32
        self.model.add(LSTM(32, return_sequences=True))  # returns a sequence of vectors of dimension 32
        self.model.add(LSTM(32))  # return a single vector of dimension 32
        self.model.add(Dense(self.nb_classes, activation='softmax'))

        self.model.compile(loss='sparse_categorical_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])

    def train(self, points, class_value):
        print("Training " + str(class_value))
        x_in = np.array([points])
        x_in.resize((1, self.timesteps, self.data_dim))
        y_train = np.array([class_value])
        self.model.fit(x_in, y_train)
        prediction = self.model.predict(x_in)
        print("Should be ", class_value)
        print("Prediction ", prediction)
        self.listener(prediction)
        