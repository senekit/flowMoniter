import psutil
import time

from flask import Blueprint
from flask import g, jsonify, request

speed_blueprint = Blueprint('speed', __name__, url_prefix='/speed' )

sum= [0,0,0,0,0,0,0,0]

@speed_blueprint.route('/sum',methods=['GET'])
def getsum():
    data = []
    data.append({
        "key": "以太网",
        "in": sum[0],
        "out": sum[1]
    })
    data.append({
        "key": "以太网 2",
        "in": sum[2],
        "out": sum[3]
    })
    data.append({
        "key": "Loopback Pseudo-Interface 1",
        "in": sum[4],
        "out": sum[5]
    })
    data.append({
        "key": "vEthernet (Default Switch)",
        "in": sum[6],
        "out": sum[7]
    })
    return jsonify(data)

@speed_blueprint.route('', methods=['GET'])
def get_speed():
    data = []
    try:
        key_info, net_in, net_out = get_rate(get_key)

        for key in key_info:
            if key != 'lo' or key == '以太网':

                # print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' % (key, net_in.get(key), net_out.get(key)))
                data.append({
                    "key": key,
                    "in": net_in.get(key),
                    "out": net_out.get(key)
                })
                if key == '以太网':
                    sum[0] += net_in.get(key)
                    sum[1] += net_out.get(key)
                elif key == '以太网 2':
                    sum[2] += net_in.get(key)
                    sum[3] += net_out.get(key)
                elif key == 'Loopback Pseudo-Interface 1':
                    sum[4] += net_in.get(key)
                    sum[5] += net_out.get(key)
                elif key == 'vEthernet (Default Switch)':
                    sum[6] += net_in.get(key)
                    sum[7] += net_out.get(key)
    except KeyboardInterrupt:
        exit()
    return jsonify(data)

def get_key():

    key_info = psutil.net_io_counters(pernic=True).keys()

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

    return key_info, recv, sent

def get_rate(func):

    key_info, old_recv, old_sent = func()
    time.sleep(1)
    key_info, now_recv, now_sent = func()

    net_in = {}
    net_out = {}

    for key in key_info:
        # float('%.2f' % a)
        net_in.setdefault(key, float('%.2f' %((now_recv.get(key) - old_recv.get(key)) / 1024)))
        net_out.setdefault(key, float('%.2f' %((now_sent.get(key) - old_sent.get(key)) / 1024)))

    return key_info, net_in, net_out