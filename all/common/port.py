from scapy.all import *
import time
import math

while 1:
    dpkt = sniff(count = 10)
    wrpcap("../pcaps/" + str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + ".pcap", dpkt)