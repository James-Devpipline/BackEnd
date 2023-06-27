from flask import request, Response, Blueprint

from controllers import personal_records_controller as controller

pr = Blueprint("pr", __name__)

@pr.route('/personal-record', methods=["POST"])
def add_pr() -> Response:
    return controller.add_personal_record(request)


@pr.route('/personal-records', methods=['GET'])
def get_all_prs() -> Response:
    return controller.get_all_personal_records(request)

    
@pr.route('/personal-record/<id>', methods=['GET'])
def get_pr(rec_id, ex_id) -> Response:
    return controller.get_personal_record(request, rec_id, ex_id)


@pr.route('/personal-record/<id>', methods=['PUT'])
def update_pr(rec_id, ex_id) -> Response:
    return controller.update_personal_record(request,rec_id, ex_id)
    

@pr.route('/personal-record/<id>', methods=['DELETE'])
def delete_pr(rec_id, ex_id) -> Response:
    return controller.delete_personal_record(request, rec_id, ex_id)
    