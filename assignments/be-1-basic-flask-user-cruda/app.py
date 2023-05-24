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

data = [{
  "id": 1,
  "first_name": "Bevan",
  "last_name": "Russon",
  "email": "brusson0@eventbrite.com",
  "gender": "Male",
  "active": 0
}, {
  "id": 2,
  "first_name": "Ivan",
  "last_name": "Cullingford",
  "email": "icullingford1@go.com",
  "gender": "Male",
  "active": 1
}, {
  "id": 3,
  "first_name": "Jarred",
  "last_name": "Del Dello",
  "email": "jdeldello2@4shared.com",
  "gender": "Male",
  "active": 0
}, {
  "id": 4,
  "first_name": "Dela",
  "last_name": "Minker",
  "email": "dminker3@ucoz.ru",
  "gender": "Female",
  "active": 0
}, {
  "id": 5,
  "first_name": "Abbey",
  "last_name": "Saggs",
  "email": "asaggs4@cbslocal.com",
  "gender": "Female",
  "active": 0
}, {
  "id": 6,
  "first_name": "Keith",
  "last_name": "Cordelet",
  "email": "kcordelet5@umn.edu",
  "gender": "Male",
  "active": 0
}, {
  "id": 7,
  "first_name": "Marc",
  "last_name": "Lazenbury",
  "email": "mlazenbury6@utexas.edu",
  "gender": "Male",
  "active": 0
}, {
  "id": 8,
  "first_name": "Rea",
  "last_name": "Trawin",
  "email": "rtrawin7@globo.com",
  "gender": "Female",
  "active": 1
}, {
  "id": 9,
  "first_name": "Kathi",
  "last_name": "Gooly",
  "email": "kgooly8@jimdo.com",
  "gender": "Agender",
  "active": 0
}, {
  "id": 10,
  "first_name": "Nissie",
  "last_name": "Ashbrook",
  "email": "nashbrook9@dyndns.org",
  "gender": "Female",
  "active": 0
}]


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
# Route to Add User to Database
@app.route('/user/add', methods=['POST'])
def user_add():
    post_data = request.get_json()
    first_name = post_data.get('first_name')
    last_name = post_data.get('last_name')
    email = post_data.get('email')
    phone = post_data.get('phone')
    city = post_data.get('city')
    state = post_data.get('state')
    org_id = post_data.get('org_id')
    active = post_data.get('active')

    add_user(first_name, last_name, email, phone, city, state, org_id, active)
    
    return jsonify("User created"), 201
