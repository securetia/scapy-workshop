#!/usr/bin/env python3

<<<<<<< HEAD
import sys

import click
from scapy.all import conf, sniff


=======
import click
import logging
import sys

from scapy.all import conf, sniff

>>>>>>> f22fc548b751bd19bbd4707980482b2514f034f4
def procpkt(pkt):
    pkt.show2()
    print('=' * 120)

@click.command()
@click.option('-i', 'iface', default=None, help='Interface to use')
def cmd_arp_sniff(iface):

    conf.verb = False
<<<<<<< HEAD
=======

>>>>>>> f22fc548b751bd19bbd4707980482b2514f034f4
    if iface:
        conf.iface = iface

    print("Waiting for ARP packets...", file=sys.stderr)
<<<<<<< HEAD
    sniff(filter="arp", store=False, prn=procpkt)

=======

    sniff(filter="arp", store=False, prn=procpkt)


>>>>>>> f22fc548b751bd19bbd4707980482b2514f034f4
if __name__ == '__main__':
    cmd_arp_sniff()
