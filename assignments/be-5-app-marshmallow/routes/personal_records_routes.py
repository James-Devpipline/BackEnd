from flask import request, Response, Blueprint

from controllers import personal_records_controller as controller

pr = Blueprint("pr", __name__)

@pr.route('/exercises/', methods=["POST"])
def add_exercise() -> Response:
    return controller.add_rec(request)


@pr.route('/exercises', methods=['GET'])
def get_all_exercises() -> Response:
    return controller.get_all_exercises(request)
    
    
@pr.route('/exercises/<id>', methods=['GET'])
def get_exercise(id) -> Response:
    return controller.get_exercise(request, id)


@pr.route('/exercises/<id>', methods=['PUT'])
def update_exercise(id) -> Response:
    return controller.get_exercise(request, id)
    

@pr.route('/exercises/<id>', methods=['DELETE'])
def delete_exercise(id) -> Response:
    return controller.delete_exercise(request, id)
    