import datetime
import jwt
from flask import request, make_response, current_app
from flask_restful import Resource
from app.user.model import User


class LoginController(Resource):

    def get(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response(
                {'message': 'Could not verify'},
                401,
                {
                    'WWW-Authenticate': 'Basic realm="Login required!"'
                }
            )

        user = User.query.filter_by(email=auth.username).first()

        if not user:
            return make_response(
                {'message': 'Could not verify'},
                401,
                {
                    'WWW-Authenticate': 'Basic realm="Login required!"'
                }
            )

        if User.verify_password(user.password, auth.password):
            token = jwt.encode({
                'uuid': user.uuid,
                'exp': datetime.datetime.utcnow()
                + datetime.timedelta(minutes=30)
            }, current_app.config['SECRET_KEY'])
            return {'token': token.decode('utf-8')}

        return make_response(
            {'message': 'Could not verify'},
            401,
            {
                'WWW-Authenticate': 'Basic realm="Login required!"'
            }
        )
