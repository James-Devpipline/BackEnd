import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from muscles import MuscleSchema
from exercise_types import ExTypeSchema

from db import db

class Exercises(db.Model):
    __tablename__ = "Exercises"

    exercise_id = db.Column(UUID (as_uuid=True), primary_key = True, default = uuid.uuid4)
    name = db.Column(db.String(), nullable = False)
    muscles_targeted = db.Column(UUID (as_uuid=True), db.ForeignKey("Muscles.muscle_id"), nullable = False)
    exercise_types = db.Column(UUID (as_uuid=True), db.ForeignKey("ExerciseTypes.type_id"), nullable = False) 
    image_url = db.Column(db.String())
    description = db.Column(db.String())

    def __init__(self, name, muscles_targeted, exercise_types, image_url, description):
        self.name = name
        self.muscles_targeted = muscles_targeted
        self.exercise_types = exercise_types
        self.image_url = image_url
        self.description = description

class ExSchema(ma.Schema):
    class Meta:
        fields = ["name", "muscles_targeted", "exercise_types", "image_url", "description"]

    muscles_targeted = ma.fields.Nested(MuscleSchema())

    exercise_types = ma.fields.Nested(ExTypeSchema())

ex_schema = ExSchema()
exs_schema = ExSchema(many=True)