import GPUtil
import time
import psutil

from flask import Blueprint
from flask import g, jsonify, request

cpu_blueprint = Blueprint('cpu', __name__, url_prefix="/cpu")


@cpu_blueprint.route('', methods=['GET'])
def get_info():
    memory = psutil.virtual_memory()
    memory_used = memory.percent
    # print(memory_used)

    gpu = GPUtil.getGPUs()

    cpu = psutil.cpu_percent(percpu=False)
    # print(cpu)
    return {
        "memory": memory_used,
        "gpu": gpu[0].memoryUtil,
        "cpu": cpu
    }
