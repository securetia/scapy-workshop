#!/usr/bin/env python3


import fnfqueue
from scapy.all import *

queue = 0

conn = fnfqueue.Connection()

try:
    q = conn.bind(queue)
    q.set_mode(0xffff, fnfqueue.COPY_PACKET)
except PermissionError:
    print("Access denied; Do I have root rights or the needed capabilities?")
    sys.exit(-1)

while True:
    for packet in conn:

        pkt = IP(packet.payload)
        pkt[TCP].show2()
        packet.accept()

conn.close()


