'''
Currently your database doesn't have a foreign key relationship set up to relate the Users and Organizations Tables. FIX THAT!
(You will have to drop your database and create it again. GET USED TO DOING THAT. We'll be doing it a lot.)
After that's done, finish your USER CRUDDA Functions and Routes
THEN do the same thing for the Organizations table!
'''

import psycopg2
from flask import Flask, jsonify, request

conn = psycopg2.connect("dbname='company-name'")
cursor = conn.cursor()

app = Flask(__name__)

def create_all():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR,
            email VARCHAR NOT NULL UNIQUE,
            phone VARCHAR,
            city VARCHAR,
            state VARCHAR,
            org_id int,
            active smallint
      );
   ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Organizations (
            org_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            phone VARCHAR,
            city VARCHAR,
            state VARCHAR,
            active smallint
      );
   ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Table_Relations (
            user_org_id SERIAL PRIMARY KEY,
            user_id int,
            org_id int,

            FOREIGN KEY (user_id)
                REFERENCES Users(user_id),

            FOREIGN KEY (org_id)
                REFERENCES Organizations(org_id)
    );
    ''')
    print("Creating tables...")
    conn.commit()

@app.route('/user/add', methods=['POST'])
def user_add():
    post_data = request.form if request.form else request.json
    first_name = post_data.get('first_name')
    last_name = post_data.get('last_name')
    email = post_data.get('email')
    phone = post_data.get('phone')
    city = post_data.get('city')
    state = post_data.get('state')
    org_id = post_data.get('org_id')
    active = post_data.get('active')

    cursor.execute("INSERT INTO Users (first_name, last_name, email,phone,  city, state, org_id, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [first_name, last_name, email, phone, city, state, org_id, active])
    conn.commit()

    return jsonify("User created"), 201


@app.route('/users', methods=['GET'])
def get_all_users():
    cursor.execute("SELECT user_id, first_name, last_name, email, phone, city, state, org_id, active FROM Users")
    results = cursor.fetchall()
    if not results:
      return jsonify("No users in db"), 400
    
    end_result = []
    for result in results:
        result_dict = {
            "user_id":result[0],
            "first_name":result[1],
            "last_name":result[2],
            "email":result[3],
            "phone":result[4],
            "city":result[5],
            "state":result[6],
            "org_id":result[7],
            "active":result[8]
        }
        end_result.append(result_dict)
    return jsonify(end_result), 200


@app.route('/users/active', methods=['GET'])
def get_active_users():
    cursor.execute(f"SELECT user_id, first_name, last_name, email, phone, city, state, org_id, active FROM Users WHERE active = 1;")
    print(cursor.execute(f"SELECT * FROM Users WHERE active = {1}"))
    results = cursor.fetchall()
    if not results:
      return jsonify("No active users in database"), 400
    
    end_result = []
    for result in results:
        result_dict = {
            "user_id":result[0],
            "first_name":result[1],
            "last_name":result[2],
            "email":result[3],
            "phone":result[4],
            "city":result[5],
            "state":result[6],
            "org_id":result[7],
            "active":result[8]
        }
        end_result.append(result_dict)
    

    return jsonify(end_result), 200


@app.route('/user/<id>', methods=["GET"])
def get_user_by_id(id):
    cursor.execute(
        "SELECT user_id, first_name, last_name, email, phone, city, state, org_id, active FROM Users WHERE user_id = %s;",
        [id])
    result = cursor.fetchone()

    if not result:
        return jsonify('That user does not exist'), 404
    else:

        result_dict = {
            "user_id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "email": result[3],
            "phone": result[4],
            "city": result[5],
            "state": result[6],
            "org_id": result[7],
            "active": result[8]
        }

        return jsonify(result_dict), 200
    

@app.route('/users/update/<user_id>', methods=['PATCH'])
def update_user(user_id):
    cursor.execute('SELECT user_id, first_name, last_name, email, phone, city, state, org_id, active FROM Users WHERE user_id = %s', [user_id])
    result = cursor.fetchone()

    if not result:
        return jsonify("User does not exist in database"), 400
    
    results_dictionary = {
        "user_id" : result[0],
        "first_name" : result[1],
        "last_name" : result[2],
        "email" : result[3],
        "phone" : result[4],
        "city" : result[5],
        "state" : result[6],
        "org_id" : result[7],
        "active" : result[8]
    }
    
    data = request.form if request.form else request.json

    for key, value in data.copy().items():
        if not value:
            data.pop(key)
    results_dictionary.update(data)

    cursor.execute('UPDATE Users SET first_name = %s, last_name = %s, email = %s, phone = %s, city = %s, state = %s, org_id = %s, active = %s WHERE user_id = %s', [results_dictionary["first_name"], results_dictionary["last_name"], results_dictionary["email"], results_dictionary["phone"], results_dictionary["city"], results_dictionary["state"], results_dictionary["org_id"], results_dictionary["active"], results_dictionary["user_id"]])

    conn.commit()
    return jsonify('User updated')


@app.route('/user/delete/<user_id>', methods=["DELETE"])
def delete_user_by_id(user_id):
    cursor.execute("DELETE FROM Users WHERE user_id = %s", [user_id])

    conn.commit()
    return jsonify('User Deleted')

# @app.route('/user/update/<id>', methods=["PUT"])
# def update_user_by_id(id):
#     cursor.execute(
#         "SELECT user_id, first_name, last_name, email, phone, city, state, org_id, active FROM Users WHERE user_id =%s;",
#         [id])
#     result = cursor.fetchone()

#     if not result:
#         return jsonify('That user does not exist'), 404
#     else:

#         result_dict = {
#             "user_id": result[0],
#             "first_name": result[1],
#             "last_name": result[2],
#             "email": result[3],
#             "phone": result[4],
#             "city": result[5],
#             "state": result[6],
#             "org_id": result[7],
#             "active": result[8]
#         }

#     data = request.form if request.form else request.json

#     for key, value in data.copy().items():
#         if not value:
#             data.pop(key)

#     result_dict.update(data)

#     cursor.execute(
#         '''UPDATE Users SET 
#         first_name = %s, 
#         last_name= %s, 
#         email= %s, 
#         phone= %s, 
#         city= %s, 
#         state= %s, 
#         org_id= %s, 
#         active= %s 
        
#         WHERE user_id = %s
#     ;''',
#         [result_dict['first_name'],
#          result_dict['last_name'],
#          result_dict["email"],
#          result_dict["phone"],
#          result_dict["city"],
#          result_dict['state'],
#          result_dict['org_id'],
#          result_dict['active'],
#          result_dict['user_id']])
#     conn.commit()
#     return jsonify('user updated')





if __name__ == "__main__":
    create_all()
    app.run(port="8086", host="0.0.0.0", debug = True)