# data type DateTime for db.column
# copy from orgs
import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
from .users import UsersSchema


class Auths(db.Model):
    __tablename__ = "AuthTokens"

    auth_token = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.user_id"), nullable=False)
    expiration = db.Column(db.DateTime(), nullable=False)

    def __init__(self, user_id, expiration):
        self.user_id = user_id
        self.expiration = expiration

    def new_auth():
        return Auths(0, "")


class AuthsSchema(ma.Schema):
    class Meta:
        fields = ['auth_token', 'user_id', 'expiration']

        user_id = ma.fields.Nested(UsersSchema)
        # user = ma.fields.Nested(UsersSchema(only=("role", "first_name", "user_id")))


auth_schema = AuthsSchema()
auths_schema = AuthsSchema(many=True)
