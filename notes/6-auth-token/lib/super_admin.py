from flask_bcrypt import generate_password_hash
from datetime import datetime

from db import db

from models.users import Users
from models.organizations import Organizations
import config


def create_super_admin():
    print("Querying for Super Admin user...")

    user_data = db.session.query(Users).filter(Users.email == 'backendn@admin.com').first()
    org_data = db.session.query(Organizations).filter(Organizations.name == config.org_name).first()
    org_id = org_data.org_id

    if user_data == None:
        print("Admin not found! Creating admin...")
        newpw = input(' Enter a password for Super Admin: ')
        password = generate_password_hash(newpw).decode("utf8")

        record = Users(first_name=config.admin_name[0], last_name=config.admin_name[1], role=config.admin_role,  phone='', email=config.admin_email, password=password, city=config.admin_city, state=config.admin_state, org_id=org_id, active=True)

        db.session.add(record)
        db.session.commit()

    else:
        print("Admin found!")
