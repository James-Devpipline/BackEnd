import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from exercises import ExSchema
from recorded_exercises import RecSchema

from db import db

class PersonalRecords(db.Model):
    __tablename__ = "PersonalRecords"

    exercise_id = db.Column(UUID (as_uuid=True), db.ForeignKey("Exercises.exercise_id"), primary_key = True, default = uuid.uuid4)
    recorded_exercise = db.Column(UUID (as_uuid=True), db.ForeignKey("RecordedExercises.recorded_id"), primary_key = True, default = uuid.uuid4, )

    def __init__(self, exercise_id, recorded_exercise):
        self.exercise_id = exercise_id
        self.recorded_exercise = recorded_exercise

class PRSchema(ma.Schema):
    class Meta:
        fields = ["exercise_id", "recorded_exercise"]

    exercise_id = ma.fields.Nested(ExSchema())
    recorded_exercise = ma.fields.Nested(RecSchema())

pr_schema = PRSchema() 
prs_schema = PRSchema(many = True) 