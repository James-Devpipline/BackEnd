from flask import request, Response, Blueprint

from controllers import exercise_types_controller as controller

ex_type = Blueprint("ex_type", __name__)


@ex_type.route('/exercise-type', methods=["POST"])
def add_ex_type() -> Response:
    return controller.add_exercise_type(request)


@ex_type.route('/exercise-types', methods=["GET"])
def get_all_ex_types() -> Response:
    return controller.get_all_exercise_types(request)


@ex_type.route('/exercise-type/<id>', methods=['GET'])
def get_ex_type(id) -> Response:
    return controller.get_exercise_type(request, id)


@ex_type.route('/exercise-type/<id>', methods=['PUT'])
def update_ex_type(id) -> Response:
    return controller.update_exercise_type(request, id)


@ex_type.route('/exercise-type/<id>', methods=['DELETE'])
def delete_ex_type(id) -> Response:
    return controller.delete_exercise_type(request, id)
