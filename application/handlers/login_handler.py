from accounts.accounts.domain.account import Account
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime


 
class LoginHandler(Resource):
    def post(self):
        pass
        # data = request.get_json()
        # # user = Users.objects.get(email=data.get('email'))
        # # auth_success = user.check_pw_hash(data.get('password'))
        # if request.json["password"] != '12345':
        #     response = jsonify({'message':'error'}),401
        #     return response
        # else:
        #     expiry = datetime.timedelta(minutes=2)
        #     access_token = create_access_token(identity=str("qwertgsa"), expires_delta=expiry)
        #     refresh_token = create_refresh_token(identity=str("qwertgsa"))
        #     return jsonify({'result': {'access_token': access_token,
        #                                'refresh_token': refresh_token,
        #                                'logged_in_as': "correo@gmail.com"}})
