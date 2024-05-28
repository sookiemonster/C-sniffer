#!/usr/bin/env python

# Import scapy library
from scapy.all import *

# TASK 1.1B
QUESTION = 2

def summarize(pkt):
   return pkt.summary()

match QUESTION:
   case 0:
      # Sniff exclusively ICMP packet
      sniff(filter='icmp', prn = lambda x : x.summary())

   case 1:
      # Sniff TCP pckets from a specified IP and dest. port of 23
      SRC:str = "255.255.255.255"
      PORT:str = "0000"
      print(f"Sniffing TCP packets from {SRC} destined for port {PORT}")
      sniff(filter=f"tcp and src {SRC} and dst port {PORT}", prn = lambda x : x.summary())

   case 2:
      SUBNET:str = "192.168.1"
      print(f'Capturing packets from / for subnet {SUBNET}')
      sniff(filter=f"net {SUBNET}", prn = lambda x : x.summary())