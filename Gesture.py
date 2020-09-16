from Data import Data
import pandas as pd
import numpy as np


class Gesture:

    def __init__(self):
        self.collection = []
        self.columns = ['Tiempo', 'Contador', 'Acx', 'Acy', 'Acz', 'Gx', 'Gy', 'Gz']
        self.quality_range = 30
        self.resume = []

    def append(self, data: tuple):
        dt = Data(data)
        self.collection.append(dt.get_all_atr())

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
