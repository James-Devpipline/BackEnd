import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class exercise_types(db.Model):
    __tablename__ = "ExerciseTypes"

    type_id = db.Column(UUID(as_uuid=True),primary_key = True, default = uuid.uuid4)
    name = db.Column(db.String(), nullable = False, unique = True)
    description = db.Column(db.String())
    image_url = db.Column(db.String())

    def __init__(self, name, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url

class ExTypeSchema(ma.Schema):
    class Meta:
        fields = ["name", "description", "image_url"]

ex_type_schema = ExTypeSchema()
ex_types_schema = ExTypeSchema(many = True)