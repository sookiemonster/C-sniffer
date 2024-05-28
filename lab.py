#!/usr/bin/env python

# Import scapy library
from scapy.all import *

# TASK 1.1B
# SRC:str = "255.255.255.0"

# Sniff exclusively ICMP packet
# sniff(filter='icmp', prn = lambda x : x.summary())

# Sniff TCP pckets from a specified IP and dest. port of 23
SRC:str = "255.255.255.255"
PORT:str = "0000"
print(f"Sniffing TCP packets from {SRC} destined for port {PORT}")
sniff(filter=f"tcp and src {SRC} and dst port {PORT}", prn = lambda x : x.summary())