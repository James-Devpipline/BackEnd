from flask import request, Response, Blueprint

from controllers import muscles_controller as controller

muscles = Blueprint("muscles", __name__)


@muscles.route('/muscle', methods=["POST"])
def add_muscle() -> Response:
    return controller.add_muscle(request)


@muscles.route('/muscles', methods=['GET'])
def get_all_muscles() -> Response:
    return controller.get_all_muscles(request)
    
    
@muscles.route('/muscle/<id>', methods=['GET'])
def get_muscle(id) -> Response:
    return controller.get_muscle(request, id)


@muscles.route('/muscle/<id>', methods=['PUT'])
def update_muscle(id) -> Response:
    return controller.update_muscle(request, id)
    

@muscles.route('/muscle/<id>', methods=['DELETE'])
def delete_muscle(id) -> Response:
    return controller.delete_muscle(request, id)
    