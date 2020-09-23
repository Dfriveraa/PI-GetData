import socket
import struct
from Gesture import Gesture
import timeit
import time

reggresive_count = 3

while reggresive_count > 0:
    print(reggresive_count)
    time.sleep(reggresive_count)
    reggresive_count = reggresive_count - 1

print('Ya')
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

socket.bind(('0.0.0.0', 8090))

count = 0
gesture = Gesture()
start_time = timeit.default_timer()
while count < 185:
    timeit.default_timer() - start_time
    content = socket.recv(180)
    count = count + 1
    gesture.append(struct.unpack('2H6h', content))

print(timeit.default_timer() - start_time)
gesture.save(name='Activacion.csv')
print(gesture.resume)

