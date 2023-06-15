from flask import Flask, request, jsonify
from db import *
import os
from users import Users
from organizations import Organizations

database_pre = os.environ.get("DATABASE_PRE")
database_addr = os.environ.get("DATABASE_ADDR")
database_user = os.environ.get("DATABASE_USER")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_user}@{database_addr}:{database_port}/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)

def create_all():
   with app.app_context():
        print("creating Tables")
        db.create_all()
        print("All Done")

@app.route('/user/add', methods=['POST'])
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


@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.session.query(Users)

    users_list = []

    for user in users:
        user_dict = {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "city": user.city,
            "state": user.state,
            "organization": {
                "org_id": user.organization.org_id,
                "name": user.organization.name,
                "phone": user.organization.phone,
                "city": user.organization.city,
                "state": user.organization.state,
                "active": user.organization.active,
            },

            "active": user.active,
        }

        users_list.append(user_dict)

    return jsonify(users_list), 200


@app.route('/users/active', methods=['GET'])
def get_active_users():
    users = db.session.query(Users).filter(Users.active == True).all()

    users_list = []

    for user in users:
        user_dict = {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "city": user.city,
            "state": user.state,
            "organization": {
                "org_id": user.organization.org_id,
                "name": user.organization.name,
                "phone": user.organization.phone,
                "city": user.organization.city,
                "state": user.organization.state,
                "active": user.organization.active,
            },

            "active": user.active,
        }
    
        users_list.append(user_dict)

    return jsonify(users_list), 200


@app.route('/user/<user_id>', methods=["GET"])
def get_user_by_id(uuid):
    user = db.session.query(Users).filter(Users.user_id == uuid).first()

    if not user:
        return jsonify("That user doesn't exist"), 404

    user_dict = {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone": user.phone,
        "city": user.city,
        "state": user.state,
        "organization": {
            "org_id": user.organization.org_id,
            "name": user.organization.name,
            "phone": user.organization.phone,
            "city": user.organization.city,
            "state": user.organization.state,
            "active": user.organization.active,
        },
        "active": user.active,
    }

    return jsonify(user_dict), 200
    

@app.route('/user/<uuid>', methods=['PATCH'])
def update_user(uuid):
    req_data = request.form if request.form else request.json

    user = db.session.query(Users).filter(Users.user_id == uuid).first()

    if not user:
        return jsonify("That user doesn't exist"), 404

    for field in req_data.keys():
        if getattr(user, field):
            setattr(user, field, req_data[field])
    
    db.session.commit()

    return jsonify("Changes made"), 200

    

@app.route('/user/delete/<uuid>', methods=["DELETE"])
def delete_user_by_id(uuid):
    user = db.session.query(Users).filter(Users.user_id == uuid).first()

    if not user:
        return jsonify("User does not exit"), 404
    
    db.session.delete(user)
    db.session.comit()

    return jsonify("User Deleted"), 200


### ORGANZITIONS ROUTES ###


@app.route('/org/add', methods=["POST"])
def add_org():
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



@app.route('/orgs', methods=["GET"])
def get_all_orgs():
    orgs = db.session.query(Organizations)

    orgs_list = []

    for org in orgs:
        org_dict = {
            'name':org.name, 
            'phone':org.phone, 
            'city':org.city, 
            'state':org.state, 
            'active':org.active
        }

        orgs_list.append(org_dict)

    return jsonify(orgs_list), 200


@app.route('/orgs/active', methods=["GET"])
def get_all_active_orgs():
    orgs = db.session.query(Organizations).filter(Organizations.active == True).all()


    orgs_list = []

    for org in orgs:
        org_dict = {
            'name':org.name, 
            'phone':org.phone, 
            'city':org.city, 
            'state':org.state, 
            'active':org.active
        }

        orgs_list.append(org_dict)
        
    return jsonify(orgs_list), 200


@app.route('/orgs/<uuid>', methods=["GET"])
def get_org_by_id(uuid):
    org_record = db.session.query(Organizations).filter(Organizations.org_id == uuid).first()

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
    

@app.route('/org/<uuid>', methods=['PATCH'])
def update_org(uuid):
    req_data = request.form if request.form else request.json

    org = db.session.query(Organizations).filter(Organizations.org_id == uuid).first()

    if not org:
        return jsonify("That organization doesn't exist"), 404

    for field in req_data.keys():
        if getattr(org, field):
            setattr(org, field, req_data[field])
    
    db.session.commit()

    return jsonify("Changes made"), 200
    

@app.route('/org/<uuid>', methods=["DELETE"])
def delete_org_by_id(uuid):
    org = db.session.query(Organizations).filter(Organizations.org_id == uuid).first()

    if not org:
        return jsonify("Organization does not exist"), 404
    
    db.session.delete(org)
    db.session.commit()

    return jsonify('Organization Deleted'), 200



if __name__ == "__main__":
    create_all()
    app.run(port="8086", host="0.0.0.0", debug = True)