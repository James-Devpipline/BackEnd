import psycopg2

conn = psycopg2.connect("dbname='usermgmt' user='james' host='localhost'") ## talks to the database
cursor = conn.cursor() ## interfaces with the dataface

def create_all():
    print("Creating tables...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL PRIMARY KEY, 
            first_name VARCHAR NOT NULL,
            last_name VARCHAR,
            email VARCHAR NOT NULL UNIQUE,
            phone VARCHAR,
            city VARCHAR,
            state VARCHAR,
            org_id INT,
            active smallint
        );
    ''')
    ## var char means varying character, this then displays as character varying. 
        ## to see this, in a shell run python app.py, then do 'psql usermgmt', then '\d "organizations"'
        ## \d means descripe
    ## smallint can either be boolean, 1 or 0

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

    conn.commit()

def add_user(first_name, last_name, email, phone, city, state, org_id, active):
    cursor.execute("INSERT INTO Users (first_name, last_name, email, phone, city, state, org_id, active) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", [first_name, last_name, email, phone, city, state, org_id, active])
    
    conn.commit()

## for what not to do in to prevent sql injection attacks go to 1:60:00 on lecture for May 18th
create_all()

add_user("James", "Hales", "test@email.com", "555-555-5555", "Spanish Fork", "UT", None, 1)