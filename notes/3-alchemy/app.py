from flask import Flask, request, jsonify
from db import *
import os

# database_uri = os.environ.get("SQLALCHEMY_DATABASE_URI")
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

def create_all():
    with app.app_context():
        print("creating Tables")
        db.create_all()
        print("All Done")

if __name__ == "__main__":
    create_all()
    app.run(port=8086, host="0.0.0.0")