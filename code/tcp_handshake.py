#!/usr/bin/env python3

import click
from scapy.all import conf, IP, TCP, L3RawSocket, sr1, RandShort


@click.command()
@click.argument('host')
@click.argument('port', type=click.INT)
def tcp_handshake(host, port):

    conf.L3socket = L3RawSocket

    l3 = IP(dst=host)
    syn = l3/TCP(sport=RandShort(), dport=port, flags='S')

    synack = sr1(syn, timeout=3, verbose=False)
    if synack[TCP].flags != 'SA':
        return False

    ack = l3/TCP(sport=synack.dport, dport=synack.sport, flags='A', seq=synack.ack, ack=synack.seq + 1)
    res = sr1(ack, timeout=3, verbose=False)
    if res:
        res[TCP].show2()

if __name__ == '__main__':
    tcp_handshake()

