import sys
sys.path.append("../../")

from application.handlers.account_handler import AccountHandler
from application.handlers.login_handler import LoginHandler
from application.handlers.artist_handler import ArtistHandler
from application.handlers.album_handler import AlbumHandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
#from flask_jwt_extended import JWTManager, jwt_required
#import jwt

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'thebiggestsecretkey'
api = Api(app)


api.add_resource(AccountHandler, '/account')
api.add_resource(ArtistHandler, '/artist')
api.add_resource(AlbumHandler, '/album')

api.add_resource(LoginHandler, '/login')



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)