from flask import Blueprint
from flask import g, jsonify, request


test_blueprint = Blueprint('test', __name__, url_prefix='/test')

@test_blueprint.before_request
def before_request():
    if request.get_data():
        g.data = request.get_json(silent=True)
    else:
        g.data = {}


@test_blueprint.route('/test', methods=['GET'])
def test():
    return 'yyy'