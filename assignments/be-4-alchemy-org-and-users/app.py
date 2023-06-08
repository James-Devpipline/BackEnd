from flask import Flask, request, jsonify
from db import *
import os
from users import Users
from organizations import Organizations

app = Flask(__name__)

def create_all():
   with app.app_context():
        print("creating Tables")
        db.create_all()
        print("All Done")

@app.route('/user/add', methods=['POST'])
def user_add():
    req_data = request.form if request.form else request.json

    fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'state', 'org_id', 'active']
    req_fields = ['name', 'email', 'org_id']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is requried'), 400
        
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

    return jsonify("User created"), 201


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
    

@app.route('/user/<user_id>', methods=['PATCH'])
def update_user(uuid):
    user = db.session.query(Users).filter(Users.user_id == uuid).first()

    if not user:
        return jsonify("User not found"), 404
    
    user_dict = {"user_id": user.user_id,
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
        "active": user.active,}

    

@app.route('/user/delete/<user_id>', methods=["DELETE"])
def delete_user_by_id(user_id):
    cursor.execute("DELETE FROM Users WHERE user_id = %s", [user_id])

    conn.commit()
    return jsonify('User Deleted')


### ORGANZITIONS ROUTES ###


@app.route('/org/add', methods=["POST"])
def add_org():
    post_data = request.form if request.form else request.json
    name = post_data.get('name')
    phone = post_data.get('phone')
    city = post_data.get('city')
    state = post_data.get('state')
    active = post_data.get('active')

    cursor.execute("INSERT INTO Organizations (name, phone, city, state, active) VALUES (%s, %s, %s, %s, %s)", [name, phone, city, state, active])
    conn.commit()

    return jsonify("Organization created"), 201


@app.route('/orgs', methods=["GET"])
def get_all_orgs():
    cursor.execute("SELECT org_id, name, phone, city, state, active FROM Organizations")
    results = cursor.fetchall()
    if not results:
      return jsonify("No Organizations in database"), 400
    
    end_result = []
    for result in results:
        result_dict = {
            "org_id":result[0],
            "name":result[1],
            "phone":result[2],
            "city":result[3],
            "state":result[4],
            "active":result[5]
        }
        end_result.append(result_dict)
    return jsonify(end_result), 200


@app.route('/orgs/active', methods=["GET"])
def get_all_active_orgs():
    cursor.execute("SELECT org_id, name, phone, city, state, active FROM Organizations WHERE active = 1;")
    results = cursor.fetchall()
    if not results:
      return jsonify("No active Organizations in database"), 400
    
    end_result = []
    for result in results:
        result_dict = {
            "org_id":result[0],
            "name":result[1],
            "phone":result[2],
            "city":result[3],
            "state":result[4],
            "active":result[5]
        }
        end_result.append(result_dict)
    

    return jsonify(end_result), 200


@app.route('/orgs/<org_id>', methods=["GET"])
def get_org_by_id(org_id):
    cursor.execute(
        "SELECT org_id, name, phone, city, state, active FROM Organizations WHERE org_id = %s;",
        [org_id])
    result = cursor.fetchone()

    if not result:
        return jsonify('That Organization does not exist'), 404
    else:
        result_dict = {
            "org_id":result[0],
            "name":result[1],
            "phone":result[2],
            "city":result[3],
            "state":result[4],
            "active":result[5]
        }

        return jsonify(result_dict), 200
    

@app.route('/org/update/<org_id>', methods=['PATCH'])
def update_org(org_id):
    cursor.execute('SELECT org_id, name, phone, city, state, active FROM Organizations WHERE org_id = %s', [org_id])
    result = cursor.fetchone()

    if not result:
        return jsonify("Organization does not exist in database"), 400
    else:
        results_dictionary = {
            "org_id":result[0],
            "name":result[1],
            "phone":result[2],
            "city":result[3],
            "state":result[4],
            "active":result[5]
        }
        
        data = request.form if request.form else request.json

        results_dictionary.update(data)

        cursor.execute('UPDATE Organizations SET name = %s, phone = %s, city = %s, state = %s, active = %s WHERE org_id = %s', [results_dictionary["name"], results_dictionary["phone"], results_dictionary["city"], results_dictionary["state"], results_dictionary["active"], results_dictionary["org_id"]])

        conn.commit()

        return jsonify('User updated')
    

@app.route('/org/delete/<org_id>', methods=["DELETE"])
def delete_org_by_id(org_id):
    cursor.execute("DELETE FROM Organizations WHERE org_id = %s", [org_id])

    conn.commit()
    return jsonify('Organization Deleted')



if __name__ == "__main__":
    create_all()
    app.run(port="8086", host="0.0.0.0", debug = True)