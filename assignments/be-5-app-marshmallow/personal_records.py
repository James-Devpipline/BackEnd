import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from recorded_exercises import RecSchema
from exercises import ExSchema

from db import db

class personal_records(db.Model):
    __tablename__ = "PersonalRecords"

    recorded_exercise = db.Column(UUID (as_uuid=True), db.ForeignKey("RecordedExercises.recorded_id"), primary_key = True, default = uuid.uuid4, )
    exercise_id = db.Column(UUID (as_uuid=True), db.ForeignKey("Exercises.exercise_id"), primary_key = True, default = uuid.uuid4)

    def __init__(self, recorded_exercise, exercise_id):
        self.recorded_exercise = recorded_exercise
        self.exercise_id = exercise_id

class PRSchema(ma.Schema):
    class Meta:
        fields = ["recorded_exercise", "exercise_id"]

    recorded_exercise = ma.fields.Nested(RecSchema())
    exercise_id = ma.fields.Nested(ExSchema())

pr_schema = PRSchema() 
prs_schema = PRSchema(many = True) 