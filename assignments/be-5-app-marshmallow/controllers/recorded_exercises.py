from flask import request, jsonify

from db import db
from models.recorded_exercises import RecordedExercises, rec_schema, recs_schema
from reflection import populate_object

@app.route('/recorded-exercises/', methods=["POST"])
def add_rec():
    req_data = request.form if request.form else request.json

    fields = ['exercise_id', 'date', 'sets', 'reps', 'distance', 'time', 'notes', 'is_personal_record', 'video_url']
    req_fields = ['exercise_id']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_rec = RecordedExercises(
        values['exercise_id'],
        values['date'],
        values['sets'],
        values['reps'],
        values['distance'],
        values['time'],
        values['notes'],
        values['is_personal_record'],
        values['video_url'])

    db.session.add(new_rec)
    db.session.commit()

    return jsonify('Exercise Recorded'), 200


@app.route('/recorded-exercises', methods=['GET'])
def get_all_recorded_exercises():
    recorded_exercises = db.session.query(RecordedExercises).filter(RecordedExercises).all()

    if not recorded_exercises:
        return jsonify('No exercises have been recorded'), 404
    else:
        return jsonify(recs_schema.dump(recorded_exercises)), 200
    

@app.route('/recorded-exercises/<id>', methods=['GET'])
def get_all_recorded_exercises(id):
    recorded_exercise = db.session.query(RecordedExercises).filter(RecordedExercises.recorded_id == id).first()

    if not recorded_exercise:
        return jsonify('That recorded exercise does not exist'), 404
    else:
        return jsonify(rec_schema.dump(recorded_exercise)), 200
    

@app.route('/recorded-exercises/<id>', methods=['PUT'])
def update_recorded_exercise(id):
    post_data = request.json
    if not post_data:
        post_data = request.form
    
    recorded_exercise = db.session.query(RecordedExercises).filter(RecordedExercises.recorded_id == id).first()

    populate_object(recorded_exercise, post_data)
    db.session.commit()

    return jsonify(rec_schema.dump(recorded_exercise)), 200


@app.route('/recorded-exercises/<id>', methods=['DELETE'])
def delete_recorded_exercise(id):
    recorded_exercise = db.session.query(RecordedExercises).filter(RecordedExercises.recorded_id == id).first()

    if recorded_exercise:
        db.session.delete(recorded_exercise)
        db.session.commit()
        return jsonify(message="Recorded Exercise has been deleted")
    else:
        return jsonify(message="Recorded exercise not found, unable to delete"), 404
