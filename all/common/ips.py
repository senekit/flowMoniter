import psutil
import time

from flask import Blueprint
from flask import g, jsonify, request
from scapy.all import *
from all.tools.deletefile import delete


ips_blueprint = Blueprint('ips', __name__, url_prefix='/ips')

@ips_blueprint.route('/delete', methods=['GET'])
def handle():
    delete()
    return "success"

