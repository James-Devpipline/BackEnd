import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    first_name = db.Column(db.String(), nulable = False)
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable = False, unique = True)
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    org_id = db.Column(UUID(as_uuid = True), db.ForeignKey("Organizations.org_id"), nullable = False)
    active = db.Column(db.Boolean(), default=True)