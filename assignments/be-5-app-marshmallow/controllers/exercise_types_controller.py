from flask import request, Request, jsonify

from db import db
from models.exercise_types import ExerciseTypes, ex_type_schema, ex_types_schema
from reflection import populate_object

def add_exercise_type(req: Request):
    req_data = request.form if request.form else request.json

    fields = ['name', 'description', 'image_url']
    req_fields = ['name']

    values = {}

    for field in fields:
        field_data = req_data.get(field)
        if field_data in req_fields and not field_data:
            return jsonify(f'{field} is required'), 400

        values[field] = field_data

    new_ex_type = ExerciseTypes(
        values['name'],
        values['description'],
        values['image_url'])

    db.session.add(new_ex_type)
    db.session.commit()

    return jsonify("Exercise Type Added"), 200


def get_all_exercise_types(req: Request):
    exercise_types = db.session.query(ExerciseTypes).filter(ExerciseTypes).all()

    if not exercise_types:
        return jsonify('No exercise types have been recorded'), 404
    else:
        return jsonify(ex_types_schema.dump(exercise_types)), 200
    

def get_exercise_type(req: Request, id):
    exercise_type = db.session.query(ExerciseTypes).filter(ExerciseTypes.type_id == id).first()

    if not exercise_type:
        return jsonify('That exercise type does not exist'), 404
    else:
        return jsonify(ex_type_schema.dump(exercise_type)), 200
    

def update_exercise_type(req: Request, id):
    post_data = request.json
    if not post_data:
        post_data = request.form
    
    exercise_type = db.session.query(ExerciseTypes).filter(ExerciseTypes.type_id == id).first()

    populate_object(exercise_type, post_data)
    db.session.commit()

    return jsonify(ex_type_schema.dump(exercise_type)), 200


def delete_exercise_type(req: Request, id):
    exercise_type = db.session.query(ExerciseTypes).filter(ExerciseTypes.type_id == id).first()

    if exercise_type:
        db.session.delete(exercise_type)
        db.session.commit()
        return jsonify(message="Exercise type has been deleted")
    else:
        return jsonify(message="Exercise type not found, unable to delete"), 404
