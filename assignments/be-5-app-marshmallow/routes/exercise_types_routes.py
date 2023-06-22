from flask import request, Response, Blueprint

from controllers import exercise_types_controller

auth = Blueprint("ex_type", __name__)