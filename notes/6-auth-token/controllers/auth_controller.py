from flask import request, jsonify, Response

from models.authorizations import Auths, auth_schema, auths_schema
from db import db
from util.reflection import populate_object
from models.users import Users
from flask_bcrypt import check_password_hash


# CREATE


def add_auth_token(req: request) -> Response:
    req_data = request.form if request.form else request.json

    if not req_data:
        return jsonify("Please enter all fields"), 401

    post_data = req.get_json()
    email = post_data.get("email")
    password = post_data.get("password")

    if not email or not password:
        return jsonify({"message": "Invalid Login"}), 401

    user_data = db.session.query(Users).filter(Users.email == req_data["email"]).first()
    is_password_valid = check_password_hash(user_data.password, password)

    # if is_password_valid == False or email == None:
    #     return jsonify({"message": "inavlid email/password"}), 401

    if email != None and is_password_valid == True:
        # new_auth = Auths.new_auth(email,password)

        auth_data = Auths(user_data.user_id)
        print(auth_data)
        # input()
        db.session.add(auth_data)
        db.session.commit()
        return jsonify("authorized"), 200

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
