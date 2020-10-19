from Data import Data
import pandas as pd
import numpy as np
import tensorflow as tf


class Gesture:
    def __init__(self):
        self.collection = []
        self.columns = ['Tiempo', 'Contador', 'Acx', 'Acy', 'Acz', 'Gx', 'Gy', 'Gz']
        self.quality_range = 30
        self.resume = []
        self.model = self.get_conv_model_A(4, 20, 60)
        self.model.load_weights('./checkpoints/checkpoint_sf60_bs100_nf20_#5')

    def append(self, data: tuple):
        dt = Data(data)
        self.collection.append(dt.get_all_atr())

    def get_conv_model_A(self, num_classes, num_filtros, size_filtros, compile = True):

        # print("using",num_classes,"classes")
        inputs = tf.keras.Input(shape=(300, 6), name="input_1")
        layers = tf.keras.layers.Conv1D(num_filtros, size_filtros, activation="relu", padding="SAME")(inputs)
        layers = tf.keras.layers.Flatten()(layers)
        layers = tf.keras.layers.Dense(16, activation=tf.nn.relu)(layers)
        layers = tf.keras.layers.Dropout(0.2)(layers)
        predictions = tf.keras.layers.Dense(num_classes, activation=tf.nn.softmax, name="output_1")(layers)
        model = tf.keras.Model(inputs=inputs, outputs=predictions)
        opt = tf.keras.optimizers.Adam(learning_rate=0.0001)
        if compile:
            model.compile(optimizer=opt,
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])
        return model

    def save(self, name: str):
        try:
            df = pd.read_csv(name)
            self.set_quality()
            df2 = pd.DataFrame(self.collection, columns=self.columns)
            df = df.append(df2, ignore_index=True)
            print('Read csv sucesfully', df.shape)

        except:

            print('Fail load csv')
            self.set_quality()
            df = pd.DataFrame(self.collection, columns=self.columns)
        df.to_csv(name, index=False)

    def set_quality(self):
        columns = np.array(self.collection)[:, 0:2]
        aux1 = columns[0, 0]
        aux2 = columns[0, 1]
        max_delay = 0
        count_out = 0
        order = True

        for i, j in columns[1:, :]:
            delay = i - aux1
            if delay > self.quality_range:
                count_out = count_out + 1

            if delay > max_delay:
                max_delay = delay

            change = j - aux2
            if change != 1.0 and change != 0.0:
                order = False
            aux2 = j
            aux1 = i
        self.resume = ['Order', order, 'Max_Delay', max_delay, 'Out_Range', count_out, '', '']
        self.collection.append(self.resume)

    def predict(self):
        aux=np.array(self.collection)[:, 2:8]

        m = np.fft.rfft(aux, axis=0)
        f = 25
        ones = np.ones(f)
        zeros = np.zeros(m.shape[0] - f)
        c = np.concatenate((ones, zeros))
        clean = m * c.reshape(m.shape[0], 1)
        m = np.fft.irfft(clean, axis=0)
        aux=np.array([m,aux])
        print(aux.shape)
        # aux = np.array(np.array(m))
        print(self.model.predict(aux))
        print(self.model.predict(aux).argsort(axis=1))