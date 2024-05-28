#!/usr/bin/env python

# Import scapy library
from scapy.all import *

QUESTION = 3

def summarize(pkt):
   return pkt.summary()

def ping(spoof_ip, dst_ip):
   # Create an IP Object
   header = IP(src = spoof_ip, dst = dst_ip)
   # Mount the ICMP data onto p
   pkt = header/ICMP()
   # Vertify the contents of the packet
   header.show()
   send(pkt)

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
      SUBNET:str = "SUBNET"
      print(f'Capturing packets from / for subnet {SUBNET}')
      sniff(filter=f"net {SUBNET}", prn = lambda x : x.summary())
   case 3: 
      ping("SRC", "DST")
