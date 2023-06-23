from flask import request, Request, jsonify

from db import db
from models.personal_records import PersonalRecords, pr_schema, prs_schema
from reflection import populate_object

def add_personal_record(req: Request):
    req_data = request.form if request.form else request.json

    fields = ['recorded_exercise', 'exercise_id']
    req_fields = ['recorded_exercise', 'exercise_id']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_pr_type = PersonalRecords(
        values['muscle_group'],
        values['image_url'])

    db.session.add(new_pr_type)
    db.session.commit()

    return jsonify("Personal Record Added"), 200


def get_all_personal_records(req: Request):
    muscles = db.session.query(PersonalRecords).filter(PersonalRecords).all()

    if not muscles:
        return jsonify('No muscles have been recorded'), 404
    else:
        return jsonify(prs_schema.dump(muscles)), 200
    

def get_personal_record(req: Request, rec_id, ex_rec_id, ex_id):
    personal_record = db.session.query(PersonalRecords).filter(PersonalRecords.recorded_exercise == rec_id, ex_id).first()

    if not personal_record:
        return jsonify('That personal record does not exist'), 404
    else:
        return jsonify(pr_schema.dump(personal_record)), 200
    

def update_personal_record(req: Request, rec_id, ex_id):
    post_data = request.json
    if not post_data:
        post_data = request.form
    
    muscle = db.session.query(PersonalRecords).filter(PersonalRecords.muscle_id == rec_id, ex_id).first()

    populate_object(muscle, post_data)
    db.session.commit()

    return jsonify(pr_schema.dump(muscle)), 200


def delete_personal_record(req: Request, rec_id, ex_id):
    muscle = db.session.query(PersonalRecords).filter(PersonalRecords.muscle_id == rec_id, ex_id).first()

    if muscle:
        db.session.delete(muscle)
        db.session.commit()
        return jsonify(message="Personal Record has been deleted")
    else:
        return jsonify(message="Personal Record not found, unable to delete"), 404
