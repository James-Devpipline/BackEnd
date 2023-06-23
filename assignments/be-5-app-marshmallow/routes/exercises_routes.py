from flask import request, Response, Blueprint

from controllers import exercises_controller as controller

ex = Blueprint("ex", __name__)

@ex.route('/exercises/', methods=["POST"])
def add_rec() -> Response:
    return controller.add_rec(request)


@ex.route('/exercises', methods=['GET'])
def get_all_exercises() -> Response:
    return controller.get_all_exercises(request)
    
    
@ex.route('/exercises/<id>', methods=['GET'])
def get_exercise(id) -> Response:
    return controller.get_exercise(request, id)


@ex.route('/exercises/<id>', methods=['PUT'])
def update_exercise(id) -> Response:
    return controller.get_exercise(request, id)
    

@ex.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id) -> Response:
    return controller.delete_exercise(request, id)
    