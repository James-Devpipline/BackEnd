from flask import request, jsonify

from models.authorizations import Authorizations, auth_schema, auths_schema
from db import db
from util.reflection import populate_object

# CREATE


def add_auth_token():
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all fields"), 401

    new_auth = Authorizations.new_auth()

    populate_object(new_auth, req_data)

    db.session.add(new_auth)
    db.session.commit()

    return jsonify(auth_schema.dump(new_auth)), 200

# READ


def get_auth_by_id(id):
    auth = db.session.query(Authorizations).filter(Authorizations.auth_token == id).first()

    if not auth:
        return jsonify("That auth doesn't exit"), 404
    else:
        return jsonify(auth_schema.dump(auth)), 200


def get_all_auths():
    auths = db.session.query(Authorizations).all()
    if not auths:
        return jsonify("There are no auths"), 404
    else:
        return jsonify(authorizations_schema.dump(auths)), 200

# UPDATE

# DEACT/ACT

# DELETE
