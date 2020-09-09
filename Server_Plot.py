import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import socket
from Data import Data

s = socket.socket()
s.bind(('0.0.0.0', 8090))
s.listen(0)

x = []
y = []

figure, ax = plt.subplots()
# line, = ax.plot(x, y)
# plt.axis([0, 4 * np.pi, -1, 1])
acx = [0]
acy = [0]
acz = [0]
gx = [0]
gy = [0]
gz = [0]


def func_animate(i):
    if len(acx) > 180:
        acx.pop(0)
        acy.pop(0)
        acz.pop(0)
        gx.pop(0)
        gy.pop(0)
        gz.pop(0)

    client, addr = s.accept()
    while True:
        content = client.recv(100)
        if len(content) == 0:
            break
        else:
            data = Data(content.decode())
            acx.append(data.x)
            acy.append(data.y)
            acz.append(data.z)
            gx.append(data.a)
            gy.append(data.b)
            gz.append(data.c)

    ax.clear()
    ax.plot(acx)
    ax.plot(acy)
    ax.plot(acz)
    ax.plot(gx)
    ax.plot(gy)
    ax.plot(gz)


ani = FuncAnimation(figure,
                    func_animate,
                    frames=10,
                    interval=30)
plt.show()

# while True:
#
#     client, addr = s.accept()
#     while True:
#         content = client.recv(100)
#         if len(content) == 0:
#             break
#         else:
#             print(content.decode())
#             data=Data(content.decode())
#             x=data.i
#             y=data.x
#     print('out')