import datetime
import os
import sys
import time

from flask import Flask, current_app, g
from flask_cors import CORS

def create_app()->Flask:

    flask_app = Flask(__name__)

    # TODO config

    # 上下文
    ctx = flask_app.app_context()
    ctx.push()

    # 跨域
    CORS(flask_app, support_credentials=True)


    # 分配路由

    from all.util.GreenPrint import GreenPrint
    from all.common.test import test_blueprint
    from all.common.cpu import cpu_blueprint
    from all.common.speed import speed_blueprint

    api = GreenPrint('api', __name__, url_prefix='')
    api.register_blueprint(test_blueprint)
    api.register_blueprint(cpu_blueprint)
    api.register_blueprint(speed_blueprint)

    flask_app.register_blueprint(api)

    return flask_app


