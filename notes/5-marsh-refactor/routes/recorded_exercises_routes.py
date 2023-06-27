from flask import request, Response, Blueprint

from controllers import recorded_exercises as controller

rec = Blueprint("re", __name__)

@rec.route('/recorded-exercise', methods=["POST"])
def add_rec() -> Response:
    return controller.add_recorded_exercise(request)


@rec.route('/recorded-exercises', methods=['GET'])
def get_all_recs() -> Response:
    return controller.get_all_recorded_exercises(request)
    
    
@rec.route('/recorded-exercise/<id>', methods=['GET'])
def get_rec(id) -> Response:
    return controller.get_recorded_exercise(request, id)


@rec.route('/recorded-exercise/<id>', methods=['PUT'])
def update_rec(id) -> Response:
    return controller.update_recorded_exercise(request, id)
    

@rec.route('/recorded-exercise/<id>', methods=['DELETE'])
def delete_rec(id) -> Response:
    return controller.delete_recorded_exercise(request, id)
    