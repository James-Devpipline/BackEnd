import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Muscles(db.Model):
    __tablename__ = "Muscles"

    muscle_id = db.Column(UUID (as_uuid=True), primary_key = True, default = uuid.uuid4)
    muscle_group = db.Column(db.String(), nullable = False)
    image_url = db.Column(db.String())

    def __init__(self, muscle_group, image_url):
        self.muscle_group = muscle_group
        self.image_url = image_url

    def new_muscle():
        return Muscles(0, "", "")
    
class MuscleSchema(ma.Schema):
    class Meta:
        fields = ["muscle_id", "muscle_group", "image_url"]

muscle_schema = MuscleSchema()
muscles_schema = MuscleSchema(many=True)