from accounts.accounts.domain.account import Account
from flask import Flask, request
from flask_restful import Resource
from functools import wraps
from accounts.accounts.application.use_cases import login_account
from infraestructure.sqlserver_repository_account import SqlServerAccountRepository
from accounts.accounts.domain.exceptions import DataBaseException, LoginFailedException, UserNotExistsException
import jwt, config, datetime


def authorization_token(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return { "error": "No token Authorization provided." }, 401
        try:
            data = jwt.decode(token, config.SECRET_KEY)
        except jwt.ExpiredSignatureError:
            return { "error": "Signature expired. Please login again." }, 401   
        except jwt.InvalidTokenError:
            return { "error": "Invalid token provided." }, 401

        return function(*args, **kwargs)
    return decorated

class LoginHandler(Resource):
    def post(self):
        usecase = login_account.LoginAccount(SqlServerAccountRepository())
        dtoclass = login_account.LoginAccountInputDto(
            request.json["user"],
            request.json["password"],
        )
        try:
            account = usecase.execute(dtoclass) 
        except UserNotExistsException as ex:
            return {"error": str(ex)}, 404
        except LoginFailedException as ex:
            return {"error": str(ex)}, 422
        except DataBaseException as ex:
            return {"error": str(ex)}, 500

        accessToken = jwt.encode({
            "account_id": account.idAccount, 
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=168)
        }, config.SECRET_KEY)

        return {"account": account.to_json(), "access_token": accessToken.decode("UTF-8") }, 200