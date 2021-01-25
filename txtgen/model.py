from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint


class Model(object):
    def __init__(self, input_shape, output_shape, epoch, batch_size):
        #self.input_shape = input_shape
        self.epochs = epoch
        self.batch_size = batch_size
        self.model = self.create_model(input_shape, output_shape)

    def create_model(self, input_shape, output_shape):
        model = Sequential()
        model.add(LSTM(256, return_sequences=True, input_shape=input_shape))
        model.add(Dropout(0.2))
        model.add(LSTM(512))
        model.add(Dropout(0.2))
        model.add(Dense(output_shape, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam')

        return model

    def train(self, X, y):
        filepath="./checkpoint/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
        checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]
        # fit the model
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, callbacks=callbacks_list)

    def test(self, filename):
        self.model.load_weights("./checkpoint/"+filename)
        