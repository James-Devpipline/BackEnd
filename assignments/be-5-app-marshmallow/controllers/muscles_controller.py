from flask import request, Request, jsonify

from db import db
from models.muscles import MuscleSchema, muscle_schema, muscles_schema
from reflection import populate_object

def add_muscle(req: Request):
    req_data = request.form if request.form else request.json

    fields = ['muscle_group', 'image_url']
    req_fields = ['muscle_group']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_muscle_type = MuscleSchema(
        values['muscle_group'],
        values['image_url'])

    db.session.add(new_muscle_type)
    db.session.commit()

    return jsonify("Muscle Added"), 200


def get_all_muscles(req: Request):
    muscles = db.session.query(MuscleSchema).filter(MuscleSchema).all()

    if not muscles:
        return jsonify('No muscles have been recorded'), 404
    else:
        return jsonify(muscles_schema.dump(muscles)), 200
    

def get_muscle(req: Request, id):
    muscle = db.session.query(MuscleSchema).filter(MuscleSchema.muscle_id == id).first()

    if not muscle:
        return jsonify('That muscle does not exist'), 404
    else:
        return jsonify(muscle_schema.dump(muscle)), 200
    

def update_muscle(req: Request, id):
    post_data = request.json
    if not post_data:
        post_data = request.form
    
    muscle = db.session.query(MuscleSchema).filter(MuscleSchema.muscle_id == id).first()

    populate_object(muscle, post_data)
    db.session.commit()

    return jsonify(muscle_schema.dump(muscle)), 200


def delete_muscle(req: Request, id):
    muscle = db.session.query(MuscleSchema).filter(MuscleSchema.muscle_id == id).first()

    if muscle:
        db.session.delete(muscle)
        db.session.commit()
        return jsonify(message="Muscle has been deleted")
    else:
        return jsonify(message="Muscle not found, unable to delete"), 404
