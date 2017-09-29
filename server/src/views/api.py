from flask import Blueprint
import json
from datetime import datetime


def decode_datetime(obj):
    if isinstance(obj, datetime):
        return int(obj.timestamp())
    raise TypeError("Type %s not serializable." % type(obj))


def create_api_views(handlers, request):
    bp = Blueprint('api_v1', __name__)

    @bp.route('/', methods=['GET'])
    def index():
        handlers.user.create_new({'id': 1})
        return json.dumps({'status': 'Alive!'}), 200

    return bp
