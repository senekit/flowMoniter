import psutil
import time

from flask import Blueprint
from flask import g, jsonify, request
from scapy.all import *


ips_blueprint = Blueprint('ips', __name__, url_prefix='/ips')
