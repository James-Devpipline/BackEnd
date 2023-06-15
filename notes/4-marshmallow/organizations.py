import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Organizations(db.Model):
    __tablename__ = "Organizations"

    org_id = db.Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4)
    name = db.Column(db.String(), nullable = False, unique = True)
    city = db.Column(db.String())
    state = db.Column(db.String())
    phone = db.Column(db.String())
    active = db.Column(db.String(), default = True)

    users = db.relationship("users", backref="organization", lazy=True)

    def __init__(self, name, city, state, phone, active):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.active = active

class OrganizationsSchema(ma.Schema):
    class Meta:
        fields = ['org_id', 'name', 'phone', 'city', 'state', 'active']

organization_schema = OrganizationsSchema() # for one organization to be dump
organizations_schema = OrganizationsSchema(many = True) # for multiple organizations to be dumped