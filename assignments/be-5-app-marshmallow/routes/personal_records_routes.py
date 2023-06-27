from flask import request, Response, Blueprint

from controllers import personal_records_controller as controller

pr = Blueprint("pr", __name__)

@pr.route('/personal-record', methods=["POST"])
def add_pr() -> Response:
    return controller.add_personal_record(request)


@pr.route('/personal-records', methods=['GET'])
def get_all_prs() -> Response:
    return controller.get_all_personal_records(request)

    
@pr.route('/personal-record/<ex_id>', methods=['GET'])
def get_pr(ex_id) -> Response:
    return controller.get_personal_record(request, ex_id)


@pr.route('/personal-record/<ex_id>', methods=['PUT'])
def update_pr(ex_id) -> Response:
    return controller.update_personal_record(request, ex_id)
    

@pr.route('/personal-record/<ex_id>', methods=['DELETE'])
def delete_pr(ex_id) -> Response:
    return controller.delete_personal_record(request, ex_id)
    