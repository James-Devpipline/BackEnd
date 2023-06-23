from flask import request, Response, Blueprint

from controllers import exercise_types_controller as controller

ex_type = Blueprint("ex_type", __name__)


@ex_type.route('/exercise-types/', methods=["POST"])
def add_exercise_type() -> Response:
    return controller.add_exercise_type(request)


@ex_type.route('/exercise-types/', methods=["GET"])
def get_all_exercise_types() -> Response:
    return controller.get_all_exercise_types(request)
    

@ex_type.route('/exercise-types/<id>', methods=['GET'])
def get_exercise_type() -> Response:
    return controller.get_exercise_type(request, id)
    

@ex_type.route('/exercise-types/<id>', methods=['PUT'])
def update_exercise_type() -> Response:
    return controller.update_exercise_type(request, id)
    

@ex_type.route('/exercise-types/<id>', methods=['DELETE'])
def delete_exercise_type() -> Response:
    return controller.delete_exercise_type(request, id)
    