import socket
import struct
from Gesture import Gesture

s = socket.socket()

s.bind(('0.0.0.0', 8090))
s.listen(0)

count = 0
gesture = Gesture()
while count < 180:
    client, addr = s.accept()
    content = client.recv(100)
    count = count + 1
    gesture.append(struct.unpack('H7h', content))
    # client.close()

gesture.save(name='Gesto1.csv')
# print("Closing connection")
# client.close()
