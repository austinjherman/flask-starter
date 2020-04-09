import json
from app.user.model import User
from flask import request, Response
from app.extensions import db, bcrypt
from marshmallow import ValidationError
from flask_restful import abort, Resource
from app.user.schema import users_schema, user_schema


def user_or_abort(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404, message="User {} doesn't exist".format(user_id))
    return user


# User
# get, update, and delete a user
class UserRoute(Resource):

    def get(self, user_id):
        user = user_or_abort(user_id)
        return user_schema.dump(user)

    def delete(self, user_id):
        user = user_or_abort(user_id)
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user)

    def put(self, user_id):

        user = User.query.filter_by(id=user_id).first()
        if not user:
            return Response(json.dumps({
                'message': 'User with id {} does not exist'.format(user_id)
            }), status=400, mimetype='application/json')

        try:
            json_input = user_schema.load(
                request.get_json(), partial=True
            )

        except ValidationError as err:
            msg = json.dumps({
                'message': err.messages,
                'valid': err.valid_data
            })
            return Response(msg, status=400, mimetype='application/json')

        for prop, value in json_input.__dict__.items():

            if prop == 'email':
                exists = User.query.filter_by(email=value).first()
                if exists:
                    return Response(json.dumps({
                        'message': 'Email already registered.'
                    }), status=400, mimetype='application/json')
                setattr(user, prop, value)

            if prop == 'password':
                setattr(user, prop, bcrypt.generate_password_hash(
                    user.password
                ).decode('utf-8'))

        db.session.commit()
        return user_schema.dump(user)


# Users
# get all users, create a new user
class UserListRoute(Resource):

    def get(self):
        all_users = User.query.all()
        return users_schema.dump(all_users)

    def post(self):

        try:
            user = user_schema.load(request.get_json())

        except ValidationError as err:
            msg = json.dumps({
                'message': err.messages,
                'valid': err.valid_data
            })
            return Response(msg, status=400, mimetype='application/json')

        exists = User.query.filter_by(email=user.email).first()
        if exists:
            return Response(json.dumps({
                'message': 'Email already registered.'
            }), status=400, mimetype='application/json')

        user.password = bcrypt.generate_password_hash(
            user.password
        ).decode('utf-8')

        db.session.add(user)
        db.session.commit()

        return Response(
            user_schema.dumps(user), status=201, mimetype='application/json'
        )
