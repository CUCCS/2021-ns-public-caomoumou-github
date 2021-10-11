#! /usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "172.16.111.1"
src_port = 35775
dst_port=int(input("please input dst_port:"))

stealth_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(stealth_scan_resp)=="None"):
    print ("The port is filtered")
elif(stealth_scan_resp.haslayer(TCP)):
    if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)			# 连接 R==>RST
        print( "Open")
    elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
        print ("Closed")
