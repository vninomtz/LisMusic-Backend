import sys
sys.path.append("../../")
from accounts.accounts.application.use_cases import create_account, update_account
from infraestructure.sqlserver_repository import SqlServerAccountRepository
import datetime
from accounts.accounts.domain.account import Account
from accounts.accounts.domain.exceptions import AccountInvalidException, DataBaseException
from flask import Flask, request, jsonify
from flask_restful import Resource, Api


class AccountHandler(Resource):
    def post(self):
        print("Creando cuenta...")
        usecase = create_account.CreateAccount(SqlServerAccountRepository())
        dtoclass = create_account.CreateAccountInputDto()
        dtoclass.firstName = request.json["firstName"]
        dtoclass.lastName = request.json["lastName"]
        dtoclass.email = request.json["email"]
        dtoclass.password = request.json["password"]
        dtoclass.userName = request.json["userName"]
        dtoclass.gender = request.json["gender"]
        dtoclass.birthday = datetime.datetime.strptime((request.json["birthday"]), '%Y-%m-%d')
        dtoclass.cover = request.json["cover"]
        try:
            result = usecase.execute(dtoclass)
            if result:
                return result.idAccount
        except (AccountInvalidException, DataBaseException) as ex:
            print(ex)

        return "Error"