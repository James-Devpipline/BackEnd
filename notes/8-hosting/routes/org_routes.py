from flask import request, Blueprint

from controllers import org_controller

org = Blueprint('org', __name__)


@org.route('/org', methods=["POST"])
def add_organization():
    return org_controller.add_organization(request)


@org.route("/org/<id>", methods=["GET"])
def get_org_by_id(id):
    return org_controller.get_org_by_id(request, id)


@org.route("/orgs", methods=["GET"])
def get_all_orgs():
    return org_controller.get_all_orgs(request)
