from flask import request, jsonify, Response

from models.authorizations import Auths, auth_schema, auths_schema
from db import db
from util.reflection import populate_object
from models.users import Users
from flask_bcrypt import check_password_hash
from datetime import datetime


# CREATE


def add_auth_token() -> Response:  # arrow is documentation, its used as this is supposed to be returned, its non binding.
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all fields"), 401

    post_data = request.get_json()
    email = post_data.get("email")
    password = post_data.get("password")

    if not email or not password:
        return jsonify({"message": "Invalid Login"}), 401

    user_data = db.session.query(Users).filter(Users.email == req_data["email"]).first()
    user_check = db.session.query(Auths).filter(Auths.user_id == user_data.user_id).all()
    is_password_valid = check_password_hash(user_data.password, password)

    if email != None and is_password_valid == True:
        if user_check:
            # tokin_check = db.session.query(Auths).filter(user_check.expiration <=  datetime.now()).all()

            # if tokin_check:
            for token in user_check:
                db.session.delete(token)  # looping through to delete all prev valid and invalid tokens incase there are any. Then create a new one. Code commented out above checks if there are any valid tokens only

        auth_data = Auths(user_data.user_id, None)
        print(auth_data)
        db.session.add(auth_data)
        db.session.commit()
        return jsonify(auth_schema.dump(auth_data)), 200

    return jsonify({"message": "Invalid Login"}), 401

# READ


def get_auth_by_id(id):
    auth = db.session.query(Auths).filter(Auths.auth_token == id).first()

    if not auth:
        return jsonify("That auth doesn't exit"), 404
    else:
        return jsonify(auth_schema.dump(auth)), 200


def get_all_auths():
    auths = db.session.query(Auths).all()
    if not auths:
        return jsonify("There are no auths"), 404
    else:
        return jsonify(auths_schema.dump(auths)), 200

# UPDATE

# DEACT/ACT

# DELETE
