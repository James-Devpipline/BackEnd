from flask import request, jsonify

from models.organizations import Organizations, organization_schema, organizations_schema
from lib.authenticate import auth
from db import db
from util.reflection import populate_object

# CREATE

@auth
def add_organization(req):
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all fields"), 401

    new_org = Organizations.new_org()

    populate_object(new_org, req_data)

    db.session.add(new_org)
    db.session.commit()

    return jsonify(organization_schema.dump(new_org)), 200

# READ

@auth
def get_org_by_id(req, id):
    org_record = db.session.query(Organizations).filter(Organizations.org_id == id).first()

    if not org_record:
        return jsonify("That organization doesn't exit"), 404
    else:
        return jsonify(organization_schema.dump(org_record)), 200

@auth
def get_all_orgs(req):
    orgs = db.session.query(Organizations).all()
    if not orgs:
        return jsonify("There are no Orgs"), 404
    else:
        return jsonify(organizations_schema.dump(orgs)), 200

# UPDATE

# DEACT/ACT

# DELETE
