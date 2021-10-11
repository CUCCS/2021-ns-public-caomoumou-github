#! /usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "172.16.111.1"
src_port = 35775
dst_port=int(input("please input dst_port:"))

tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)

if(str(tcp_connect_scan_resp)=="None"):
    print( "The port is filtered")
elif(tcp_connect_scan_resp.haslayer(TCP)):
    if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
        send_ack = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="A",ack=(tcp_connect_scan_resp[TCP].seq+1)),timeout=10)
        send_rst = sr(IP(dst=dst_ip)/  	   TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)# 全连接 AR => ACK+RST
        print( "Open")
    elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
    	print( "Closed")