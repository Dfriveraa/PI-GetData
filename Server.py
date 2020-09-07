import socket
import time
from Gesture import Gesture
from Data import Data

s = socket.socket()

s.bind(('0.0.0.0', 8090))
s.listen(0)


count=0
gesture=Gesture()
while count<118:

    client, addr = s.accept()
    while True:
        content = client.recv(100)

        if len(content) == 0:
            break

        else:
            count=count+1
            gesture.append(content.decode())
gesture.to_pd(name='1test.csv')
    # print("Closing connection")
    # client.close()