from Data import Data
import pandas as pd


class Gesture:

    def __init__(self):
        self.collection = []

    def append(self, data: str):
        dt = Data(data)
        self.collection.append(dt.get_all_atr())

    def to_pd(self,name:str):
        pd.DataFrame(self.collection).to_csv(name)
        print(pd.DataFrame(self.collection))
