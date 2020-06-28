import sys
sys.path.append("../../")
<<<<<<< HEAD
from application.read.handlers.playlist_handler import PlaylistAccountHandler, PlaylistTracksHandler
from application.read.handlers.album_handler import AlbumsOfArtistHandler, TracksOfAlbumHandler
=======
from application.read.handlers.playlist_handler import PlaylistAccountHandler
from application.read.handlers.album_handler import AlbumsOfAccount, AlbumsOfArtistHandler, TracksOfAlbumHandler
>>>>>>> dff0b1c30b8e872093b32a57f1b8f3ee04c2336f
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


api.add_resource(PlaylistAccountHandler, '/account/<string:idAccount>/playlist')
api.add_resource(AlbumsOfArtistHandler, '/artist/<string:idArtist>/album')
api.add_resource(TracksOfAlbumHandler, '/album/<string:idAlbum>/track')
<<<<<<< HEAD
api.add_resource(PlaylistTracksHandler, '/playlist/<int:idPlaylist>/tracks')
=======
api.add_resource(AlbumsOfAccount, '/account/<string:idAccount>/album')
>>>>>>> dff0b1c30b8e872093b32a57f1b8f3ee04c2336f





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)