from flask import request, Response, Blueprint

from controllers import exercises_controller as controller

ex = Blueprint("ex", __name__)


@ex.route('/exercise', methods=["POST"])
def add_exercise() -> Response:
    return controller.add_exercise(request)


@ex.route('/exercises', methods=['GET'])
def get_all_exercises() -> Response:
    return controller.get_all_exercises(request)
    
    
@ex.route('/exercise/<id>', methods=['GET'])
def get_exercise(id) -> Response:
    return controller.get_exercise(request, id)


@ex.route('/exercise/<id>', methods=['PUT'])
def update_exercise(id) -> Response:
    return controller.update_exercise(request, id)
    

@ex.route('/exercise/<id>', methods=['DELETE'])
def delete_exercise(id) -> Response:
    return controller.delete_exercise(request, id)
    