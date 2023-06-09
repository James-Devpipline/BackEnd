from flask import request, Request, jsonify

from db import db
from models.muscles import Muscles, muscle_schema, muscles_schema
from util.reflection import populate_object


def add_muscle(req: Request):
    req_data = request.form if request.form else request.json

    fields = ['muscle_group', 'image_url']
    req_fields = ['muscle_group']

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

    new_muscle = Muscles.new_muscle()

    populate_object(new_muscle, req_data)

    db.session.add(new_muscle)
    db.session.commit()

    return jsonify("Muscle Added"), 200


def get_all_muscles(req: Request):
    muscles = db.session.query(Muscles).all()

    if not muscles:
        return jsonify('No muscles have been recorded'), 404
    else:
        return jsonify(muscles_schema.dump(muscles)), 200


def get_muscle(req: Request, id):
    muscle = db.session.query(Muscles).filter(Muscles.muscle_id == id).first()

    if not muscle:
        return jsonify(message="That muscle does not exist"), 404
    else:
        return jsonify(muscle_schema.dump(muscle)), 200


def update_muscle(req: Request, id):
    post_data = request.json
    if not post_data:
        post_data = request.form

    muscle = db.session.query(Muscles).filter(Muscles.muscle_id == id).first()

    if not muscle:
        return jsonify(message="That muscle does not exist"), 404
    else:
        populate_object(muscle, post_data)
        db.session.commit()
        return jsonify(muscle_schema.dump(muscle)), 200


def delete_muscle(req: Request, id):
    muscle = db.session.query(Muscles).filter(Muscles.muscle_id == id).first()

    if muscle:
        db.session.delete(muscle)
        db.session.commit()
        return jsonify(message="Muscle has been deleted"), 200
    else:
        return jsonify(message="Muscle not found, unable to delete"), 404
