from flask import request, Request, jsonify

from db import db
from models.recorded_exercises import RecordedExercises, rec_schema, recs_schema
from util.reflection import populate_object


def add_recorded_exercise(req: Request):
    req_data = request.form if request.form else request.json

    fields = ['exercise_id', 'date', 'sets', 'reps', 'distance', 'time', 'notes', 'is_personal_record', 'video_url']
    req_fields = ['exercise_id']

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

    new_recorded_exercise = RecordedExercises.new_recorded_exercise()

    populate_object(new_recorded_exercise, req_data)

    db.session.add(new_recorded_exercise)
    db.session.commit()

    return jsonify('Exercise Recorded'), 200


def get_all_recorded_exercises(req: Request):
    recorded_exercises = db.session.query(RecordedExercises).all()

    if not recorded_exercises:
        return jsonify('No exercises have been recorded'), 404
    else:
        return jsonify(recs_schema.dump(recorded_exercises)), 200


def get_recorded_exercise(req: Request, id):
    recorded_exercise = db.session.query(RecordedExercises).filter(RecordedExercises.recorded_id == id).first()

    if not recorded_exercise:
        return jsonify('That recorded exercise does not exist'), 404
    else:
        return jsonify(rec_schema.dump(recorded_exercise)), 200


def update_recorded_exercise(req: Request, id):
    post_data = request.json
    if not post_data:
        post_data = request.form

    recorded_exercise = db.session.query(RecordedExercises).filter(RecordedExercises.recorded_id == id).first()

    if not recorded_exercise:
        return jsonify(message="Recorded exercise not found, unable to edit"), 404
    else:
        populate_object(recorded_exercise, post_data)
        db.session.commit()
        return jsonify(rec_schema.dump(recorded_exercise)), 200


def delete_recorded_exercise(req: Request, id):
    recorded_exercise = db.session.query(RecordedExercises).filter(RecordedExercises.recorded_id == id).first()

    if recorded_exercise:
        db.session.delete(recorded_exercise)
        db.session.commit()
        return jsonify(message="Recorded Exercise has been deleted")
    else:
        return jsonify(message="Recorded exercise not found, unable to delete"), 404
