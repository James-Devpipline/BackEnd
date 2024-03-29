from flask import request, Blueprint

from controllers import user_controller

user = Blueprint('user', __name__)


@user.route('/user/add', methods=["POST"])
def add_user():
    return user_controller.add_user(request)


@user.route('/users', methods=['GET'])
def get_all_active_users():
    return user_controller.get_all_active_users(request)


@user.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    return user_controller.get_user_by_id(request, id)


@user.route('/user/<id>', methods=["PUT"])
def update_user(id):
    return user_controller.update_user(request, id)
