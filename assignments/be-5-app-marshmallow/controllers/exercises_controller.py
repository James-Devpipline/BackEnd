from flask import request, Request, jsonify

from db import db
from models.exercises import Exercises, ex_schema, exs_schema
from reflection import populate_object


def add_exercise(req: Request):
    req_data = request.form if request.form else request.json

    fields = ['name', 'muscles_targeted', 'exercise_types', 'image_url', 'description']
    req_fields = ['name', 'muscles_targeted', 'exercise_types']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_exercise = Exercises(
        values['name'],
        values['muscles_targeted'],
        values['exercise_types'],
        values['image_url'],
        values['description'])

    db.session.add(new_exercise)
    db.session.commit()

    return jsonify('Exercise Recorded'), 200


def get_all_exercises(req: Request):
    exercises = db.session.query(Exercises).all()

    if not exercises:
        return jsonify('No exercises have been recorded'), 404
    else:
        return jsonify(exs_schema.dump(exercises)), 200


def get_exercise(req: Request, id):
    exercise = db.session.query(Exercises).filter(Exercises.exercise_id == id).first()

    if not exercise:
        return jsonify('That exercise does not exist'), 404
    else:
        return jsonify(ex_schema.dump(exercise)), 200


def update_exercise(req: Request, id):
    post_data = request.json
    if not post_data:
        post_data = request.form

    exercise = db.session.query(Exercises).filter(Exercises.exercise_id == id).first()

    if not exercise:
        return jsonify("Exercise not found")
    else:
        populate_object(exercise, post_data)
        db.session.commit()
        return jsonify(ex_schema.dump(exercise)), 200


def delete_exercise(req: Request, id):
    exercise = db.session.query(Exercises).filter(Exercises.exercise_id == id).first()

    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        return jsonify(message="Exercise has been deleted")
    else:
        return jsonify(message="Exercise not found, unable to delete"), 404
