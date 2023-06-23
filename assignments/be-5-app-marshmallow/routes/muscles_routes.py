from flask import request, Response, Blueprint

from controllers import muscles_controller as controller

muscles = Blueprint("muscles", __name__)


@muscles.route('/muscles/', methods=["POST"])
def add_muscle() -> Response:
    return controller.add_muscle(request)


@muscles.route('/muscles', methods=['GET'])
def get_all_muscles() -> Response:
    return controller.get_all_muscles(request)
    
    
@muscles.route('/muscles/<id>', methods=['GET'])
def get_muscles(id) -> Response:
    return controller.get_muscle(request, id)


@muscles.route('/muscles/<id>', methods=['PUT'])
def update_muscles(id) -> Response:
    return controller.get_muscle(request, id)
    

@muscles.route('/muscles/<id>', methods=['DELETE'])
def delete_muscles(id) -> Response:
    return controller.delete_muscle(request, id)
    