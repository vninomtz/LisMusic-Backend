import sys
sys.path.append("../../")
from application.read.handlers.playlist_handler import PlaylistAccountHandler
from application.read.handlers.album_handler import AlbumsOfArtistHandler, TracksOfAlbumHandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


api.add_resource(PlaylistAccountHandler, '/account/<string:idAccount>/playlist')
api.add_resource(AlbumsOfArtistHandler, '/artist/<string:idArtist>/album')
api.add_resource(TracksOfAlbumHandler, '/album/<string:idAlbum>/track')





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)