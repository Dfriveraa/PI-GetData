import socket
import struct
from Gesture import Gesture
import timeit
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

socket.bind(('0.0.0.0', 8090))

while True:
    content = socket.recv(180)
    a=struct.unpack('2H6h', content)
    # print(a[5],a[6],a[7])
    print(a)


