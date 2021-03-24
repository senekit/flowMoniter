from all import create_app
from scapy.all import *
import time
import math
import _thread

flask_app = create_app()


def catch_pcap():
    while 1:
        dpkt = sniff(count=10)
        wrpcap("all/pcaps/" + str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + ".pcap", dpkt)


if __name__ == '__main__':
    flask_app.run("127.0.0.1", port=3211, debug=True)
