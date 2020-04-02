from marshmallow import fields
from app.extensions import db, ma


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String())

    def __repr__(self):
        return '<User %r>' % self.email


class UserSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user_detail", id="<id>"),
            "collection": ma.URLFor("users")
        }
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
