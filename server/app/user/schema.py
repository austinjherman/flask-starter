from app.extensions import ma
from app.user.model import User
from marshmallow import fields, post_load


class UserSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    class Meta:
        load_only = ['password']

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
