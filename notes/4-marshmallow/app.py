from flask import Flask, request, jsonify
from db import *
import os
from users import Users, users_schema, user_schema
from organizations import Organizations, organizations_schema, organization_schema
from flask_marshmallow import Marshmallow

# python3 -m pipenv shell
# pipenv install flask flask_sqlalchemy sqlalchemy
# pipenv install psycopg2


database_pre = os.environ.get("DATABASE_PRE")
database_addr = os.environ.get("DATABASE_ADDR")
database_user = os.environ.get("DATABASE_USER")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")
# database_name = "alchemy"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_user}@{database_addr}:{database_port}/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://<username>@<ipaddress>:5432/<database>'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

def create_all():
    with app.app_context():
        print("creating Tables")
        db.create_all()
        print("All Done")

@app.route('/orgs/add', methods=["POST"])
def add_organization():
    req_data = request.form if request.form else request.json

    fields = ['name', 'phone', 'city', 'state', 'active']
    req_fields = ['name']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_org = Organizations(values['name'], values['city'], values['state'], values['phone'], values['active'])
    db.session.add(new_org)
    db.session.commit()

    return jsonify('Organization Created'), 200


@app.route('/user/add', methods=["POST"])
def add_user():
    req_data = request.form if request.form else request.json

    fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'state', 'org_id', 'active']
    req_fields = ['name', 'email', 'org_id']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_user = Users(
        values['first_name'],
        values['last_name'],
        values['email'],
        values['phone'],
        values['city'],
        values['state'],
        values['org_id'],
        values['active'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify('User Created'), 200

@app.route("/orgs/get", methods=["GET"])
def get_all_orgs():
    orgs = db.session.query(Organizations).all()
    if not orgs:
        return jsonify("There are no orgs"), 404
    else:
        return jsonify(organizations_schema.dump(orgs))

@app.route("/org/get/<id>", methods=["GET"])
def get_org_by_id(id):
    org_record = db.session.query(Organizations).filter(Organizations.org_id == id).first()

    if not org_record:
        return jsonify("That organization doesn't exit"), 404

    org_record_dict = {
        "org_id": org_record.org_id,
        "name": org_record.name,
        "phone": org_record.phone,
        "city": org_record.city,
        "state": org_record.state,
        "active": org_record.active,
    }

    return jsonify(org_record_dict), 200


@app.route('/users', methods=['GET'])
def get_all_active_users():
    users = db.session.query(Users).filter(Users.active == True).all()

    if not users:
        return jsonify('No Users Exist'), 404
    else:
        return jsonify(users_schema.dump(users)), 200


@app.route("/user/get/<id>", methods=["GET"])
def get_users_by_id(id):
    user = db.session.query(Users).filter(Users.user_id == id).first()

    if not user:
        return jsonify("That user doesn't exist"), 404
    else:
        return jsonify(user_schema.dump(user)), 200
    



if __name__ == "__main__":
    create_all()
    app.run(port=8086, host="0.0.0.0", debug=True)