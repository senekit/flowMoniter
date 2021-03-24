from all import create_app
from scapy.all import *
import time
import math
import _thread

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run("127.0.0.1", port=3211, debug=True)

