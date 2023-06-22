from flask import request, Response, Blueprint

from controllers import exercises_controller

auth = Blueprint("ex", __name__)