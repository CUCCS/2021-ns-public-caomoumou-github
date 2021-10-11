#! /usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "172.16.111.1"
src_port = 35775
dst_port=int(input("please input dst_port:"))
dst_timeout=10

def udp_scan(dst_ip,dst_port,dst_timeout):
    udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
    if (str(udp_scan_resp)=="None"):
        retrans = []
        for count in range(0,3):
            retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout))
        for item in retrans:
            if (str(item)!="None"):
                udp_scan(dst_ip,dst_port,dst_timeout)
        return ("The port is open or Filtered or closed")
    elif (udp_scan_resp.haslayer(UDP)):
        return( "Open")


print(udp_scan(dst_ip,dst_port,dst_timeout))