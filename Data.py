class Data:

    def __init__(self, data: str):
        array = self.decode(data)
        self.i = float(array[0])
        self.x = float(array[1])
        self.y = float(array[2])
        self.z = float(array[3])
        self.a = float(array[4])
        self.b = float(array[5])
        self.c = float(array[6])


    def get_all_atr(self):
        return [self.i,self.x,self.y,self.z,self.a,self.b,self.c]


    def decode(self, datos: str):
        decoded = datos.split(',')
        return decoded

