from flask import request, Response, Blueprint

from controllers import recorded_exercises as controller

rec = Blueprint("re", __name__)

@rec.route('/recorded-exercises/', methods=["POST"])
def add_rec() -> Response:
    return controller.add_rec(request)


@rec.route('/recorded-exercises', methods=['GET'])
def get_all_recorded_exercises() -> Response:
    return controller.get_all_recorded_exercises(request)
    
    
@rec.route('/recorded-exercises/<id>', methods=['GET'])
def get_recorded_exercise(id) -> Response:
    return controller.get_recorded_exercise(request, id)


@rec.route('/recorded-exercises/<id>', methods=['PUT'])
def update_recorded_exercise(id) -> Response:
    return controller.get_recorded_exercise(request, id)
    

@rec.route('/recorded-exercises/<id>', methods=['DELETE'])
def delete_recorded_exercise(id) -> Response:
    return controller.delete_recorded_exercise(request, id)
    