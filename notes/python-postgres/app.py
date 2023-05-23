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
    ## var char means variety character
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


create_all()