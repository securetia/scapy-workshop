#!/usr/bin/env python3

import sys
import click
from scapy.all import conf, sniff

def procpkt(pkt):
    pkt.show2()
    print('=' * 120)

@click.command()
@click.option('-i', 'iface', default=None, help='Interface to use')
def cmd_arp_sniff(iface):

    conf.verb = False
    if iface:
        conf.iface = iface

    print("Waiting for ARP packets...", file=sys.stderr)
    sniff(filter="arp", store=False, prn=procpkt)

if __name__ == '__main__':
    cmd_arp_sniff()
