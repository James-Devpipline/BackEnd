from flask import Flask, request, jsonify
from db import *
import os
from flask_marshmallow import Marshmallow

from models.exercises import Exercises
from models.exercise_types import ExerciseTypes
from models.muscles import Muscles
from models.personal_records import PersonalRecords
from models.recorded_exercises import RecordedExercises
import routes

# python3 -m pipenv install flask flask_sqlalchemy sqlalchemy psycopg2 marshmallow flask-marshmallow marshmallow-sqlalchemy

database_pre = os.environ.get("DATABASE_PRE")
database_addr = os.environ.get("DATABASE_ADDR")
database_user = os.environ.get("DATABASE_USER")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")
# database_name = "shipsatsea"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_user}@{database_addr}:{database_port}/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

def create_all():
    with app.app_context():
        print("creating Tables")
        db.create_all()
        print("All Done")

app.register_blueprint(routes.ex_type)
app.register_blueprint(routes.ex)
app.register_blueprint(routes.muscles)
app.register_blueprint(routes.pr)
app.register_blueprint(routes.rec)

if __name__ == "__main__":
    create_all()
    app.run(port=8086, host="0.0.0.0", debug=True)