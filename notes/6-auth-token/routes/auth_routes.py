from flask import request, Blueprint

from controllers import auth_controller

auth = Blueprint('Auth', __name__)


@auth.route('/auth/add', methods=["POST"])
def add_authorization():
    return auth_controller.add_auth_token()


@auth.route("/auth/get/<id>", methods=["GET"])
def get_auth_by_id(id):
    return auth_controller.get_auth_by_id(id)


@auth.route("/auths/get", methods=["GET"])
def get_all_auths():
    return auth_controller.get_all_auths()
