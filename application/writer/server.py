import sys
sys.path.append("../../")


from application.writer.handlers.account_handler import AccountHandler
from application.writer.handlers.login_handler import LoginHandler
from application.writer.handlers.artist_handler import ArtistHandler
from application.writer.handlers.album_handler import AlbumHandler
from application.writer.handlers.playlist_handler import PlaylistHandler
from application.writer.handlers.playlist_tracks_handler import PlaylistTracksHandler
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
api.add_resource(PlaylistHandler, '/playlist', '/playlist/<int:idPlaylist>')
api.add_resource(PlaylistTracksHandler, '/playlist/<int:idPlaylist>/track/<string:idTrack>')



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
