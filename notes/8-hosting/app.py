from flask import Flask, request, jsonify
from db import *
import os
from flask_marshmallow import Marshmallow

from models.users import Users, user_schema, users_schema
from models.organizations import Organizations, organizations_schema, organization_schema
from models.authorizations import Auths, auth_schema, auths_schema
from util.reflection import populate_object
from routes.org_routes import org
from routes.user_routes import user
from routes.auth_routes import auth
from lib.super_admin import create_super_admin
from lib.evil_inc import create_default_org


database_pre = os.environ.get("DATABASE_PRE")
database_addr = os.environ.get("DATABASE_ADDR")
database_user = os.environ.get("DATABASE_USER")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")
database_pass = os.environ.get("DATABASE_PASS")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_user}:{database_pass}@{database_addr}:{database_port}/{database_name}" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

app.register_blueprint(org)
app.register_blueprint(user)
app.register_blueprint(auth)


def create_all():
    with app.app_context():
        print("Creating Tables")
        db.create_all()
        create_default_org()
        create_super_admin()
        print("All Done")


create_all()
if __name__ == "__main__":
    app.run(port=8086, host="0.0.0.0", debug=True)
