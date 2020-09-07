class Data:

    def __init__(self, data: str):
        array = self.decode(data)
        self.i = array[0]
        self.x = array[1]
        self.y = array[2]
        self.z = array[3]
        self.a = array[4]
        self.b = array[5]
        self.c = array[6]


    def get_all_atr(self):
        return [self.i,self.x,self.y,self.z,self.a,self.b,self.c]


    def decode(self, datos: str):
        decoded = datos.split(',')
        return decoded

