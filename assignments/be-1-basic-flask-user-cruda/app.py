# Create the Database
# 1. Write a function that will get all active users from the database and return them as a list of dictionaries.
# 2. Turn your function into an endpoint at /users/get/ and test it.
# 3. Create an update function that takes a variable number of fields and updates a user record accordingly (only the fields that were passed in.)
# Turn that function into an API endpoint
# 4. Create functions for delete, activate and deactivate users
# 5. Turn those into API endpoints


# BONUS POINTS IF YOU DO ORGS TOO

import psycopg2
from flask import Flask, request, jsonify

conn = psycopg2.connect("dbname='company-name'")
cursor = conn.cursor()


def create_all():
   cursor.execute("""
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
   """)
   cursor.execute("""
      CREATE TABLE IF NOT EXISTS Organizations (
         org_id SERIAL PRIMARY KEY,
         name VARCHAR NOT NULL,
         phone VARCHAR,
         city VARCHAR,
         state VARCHAR,
         active smallint
      );
   """)
   print("Creating tables...")
   conn.commit()

create_all()

app = Flask(__name__)

# Route to Add User to Database
@app.route('/user/add', methods=['POST'])
def user_add():
    post_data = request.form if request. form else request.json
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
    
    return jsonify(post_data), 201


@app.route('/users', methods=['GET'])
def get_all_users():
    cursor.execute("SELECT * FROM Users")
    results = cursor.fetchall()
    if not results:
      return jsonify("No users in db"), 400
    
    end_result = []
    for result in results:
        result_dict = {
            "user_id":result[0],
            "first_name":result[1],
            "last_name":results[2],
            "email":result[3],
            "phone":result[4],
            "city":result[5],
            "state":result[6],
            "org_id":result[7],
            "active":result[8]
        }
        end_result.append(result_dict)
    return jsonify(end_result), 200


@app.route('/users/get/active', methods=['GET'])
def get_active_users():
    cursor.execute(f"SELECT * FROM Users WHERE active = {1}")
    results = cursor.fetchall()
    if not results:
      return jsonify("No users in db"), 400
    
    end_result = []
    for result in results:
        result_dict = {
            "user_id":result[0],
            "first_name":result[1],
            "last_name":results[2],
            "email":result[3],
            "phone":result[4],
            "city":result[5],
            "state":result[6],
            "org_id":result[7],
            "active":result[8]
        }
        end_result.append(result_dict)
    

    return jsonify(end_result), 200


@app.route('/users/update/<user_id>', methods=['GET','PATCH'])
def update_user(user_id):
    data = request.form if request.form else request.json
    
    cursor.execute('SELECT FROM Users WHERE user_id = %s', [user_id])
    result = cursor.fetchone()
    if not result:
        return jsonify("User cannot be updated as user does not exist"), 400
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    city = data.get('city')
    state = data.get('state')
    org_id = data.get('org_id')
    active = data.get('active')

    cursor.execute('UPDATE Users SET first_name = %s, last_name = %s, email = %s, phone = %s, city = %s, state = %s, org_id = %s, active = %s WHERE user_id = %s', [first_name, last_name, email, phone, city, state, org_id, active, user_id])


if __name__ == "__main__":
    app.run(port="8086", host="0.0.0.0", debug = True)
    
