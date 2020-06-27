import sys
sys.path.append("")
from application.read.handlers.PlaylistHandler import PlaylistAccountHandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


api.add_resource(PlaylistAccountHandler, '/account/<string:idAccount>/playlist')




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)