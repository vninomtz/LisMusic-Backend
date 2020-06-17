import sys
sys.path.append("../")

from application.handlers.Account import AccountHandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api.add_resource(AccountHandler, '/account')



if __name__ == "__main__":
    app.run(port='5000')