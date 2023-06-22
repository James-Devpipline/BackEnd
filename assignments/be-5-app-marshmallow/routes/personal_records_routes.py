from flask import request, Response, Blueprint

from controllers import personal_records_controller

auth = Blueprint("pr", __name__)