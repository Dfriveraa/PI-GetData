class Data:

    def __init__(self, data: tuple):

        self.t = float(data[0])
        self.i = float(data[1])
        self.x = float(data[2])
        self.y = float(data[3])
        self.z = float(data[4])
        self.a = float(data[5])
        self.b = float(data[6])
        self.c = float(data[7])


    def get_all_atr(self):
        return [self.t,self.i,self.x,self.y,self.z,self.a,self.b,self.c]

