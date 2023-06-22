from flask import request, Response, Blueprint

from controllers import recorded_exercises

auth = Blueprint("re", __name__)