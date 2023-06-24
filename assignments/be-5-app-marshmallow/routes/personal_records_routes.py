from flask import request, Response, Blueprint

from controllers import personal_records_controller

pr = Blueprint("pr", __name__)