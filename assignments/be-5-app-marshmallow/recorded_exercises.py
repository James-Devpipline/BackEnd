import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from exercises import ExSchema

from db import db

class RecordedExercises(db.Model):
    __tablename__ = "RecordedExercises"

    recorded_id = db.Column(UUID(as_uuid=True),primary_key = True, default = uuid.uuid4)
    exercise_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Exercises.exercise_id"), nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    sets = db.Column(db.String())
    reps = db.Column(db.String())
    distance = db.Column(db.String())
    time = db.Column(db.String())
    notes = db.Column(db.String())
    is_personal_record = db.Column(db.Boolean(), default = False)
    video_url = db.Column(db.String())

    def __init__(self, exercise_id, date, sets, reps, distance, time, notes, is_personal_record, video_url):
        self.exercise_id = exercise_id
        self.date = date
        self.sets = sets
        self.reps = reps
        self.distance = distance
        self.time = time
        self.notes = notes
        self.is_personal_record = is_personal_record
        self.video_url = video_url

class RecSchema(ma.Schema):
    class Meta:
        fields = ["recorded_id", "exercise_id", "date", "sets", "reps", "distance", "time", "notes", "is_personal_record", "video_url"]

    exercise_id = ma.fields.Nested(ExSchema())


rec_schema = RecSchema()
recs_schema = RecSchema(many = True)