import sys
sys.path.append("../../")
from accounts.accounts.application.use_cases import create_account, update_account, delete_account
from infraestructure.sqlserver_repository_account import SqlServerAccountRepository
import datetime
from accounts.accounts.domain.account import Account
from accounts.accounts.domain.exceptions import AccountInvalidException, DataBaseException, AccountNotExistException
from accounts.accounts.domain.exceptions import EmailAlreadyExistException, UserNameAlreadyExistException
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, jwt_required


class AccountHandler(Resource):
    def post(self):
        print("Creando cuenta...")
        usecase = create_account.CreateAccount(SqlServerAccountRepository())
        dtoclass = create_account.CreateAccountInputDto(
            None,
            request.json["firstName"],
            request.json["lastName"],
            request.json["email"],
            request.json["password"],
            request.json["userName"],
            request.json["gender"],
            datetime.datetime.strptime((request.json["birthday"]), '%Y-%m-%d'),
            request.json["cover"],
            request.json["typeRegister"]
        )


        
        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify(result.to_json())
                response.status_code = 200
                return response
        except EmailAlreadyExistException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except UserNameAlreadyExistException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except DataBaseException:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response
        except Exception:
            return {"error":"Server connection error"}

    def put(self):
        print("Actualizando cuenta...")
        usecase = update_account.UpdateAccount(SqlServerAccountRepository())
        dateAccount = None
        if request.json["birthday"]:
            dateAccount = datetime.datetime.strptime((request.json["birthday"]), '%Y-%m-%d')
        dtoclass = update_account.UpdateAccountInputDto(
            request.json["idAccount"],
            request.json["firstName"],
            request.json["lastName"],
            request.json["userName"],
            request.json["gender"],
            dateAccount,
            request.json["cover"]
        )
        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify({'message': 'Account successfully updated'})
                response.status_code = 204
                return response
        except AccountInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except AccountNotExistException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response


    def delete(self):
        print("Eliminando cuenta...")
        usecase = delete_account.DeleteAccount(SqlServerAccountRepository())
        dtoclass = delete_account.DeleteAccountInputDto(request.json["idAccount"])
        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify({'message': 'Account successfully deleted'})
                response.status_code = 204
                return response
        except AccountInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except AccountNotExistException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response
