from app.extensions import ma
from app.user.model import User
from marshmallow import fields, post_load


class UserSchema(ma.Schema):
    id = fields.Int()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    uuid = fields.String(dump_only=True)
    password = fields.String(required=True)

    class Meta:
        load_only = ['password', 'id']

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
