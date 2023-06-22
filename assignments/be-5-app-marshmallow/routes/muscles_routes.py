from flask import request, Response, Blueprint

from controllers import muscles_controller

auth = Blueprint("muscles", __name__)