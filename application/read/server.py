import sys
sys.path.append("../../")
from application.read.handlers.playlist_handler import PlaylistAccountHandler, PlaylistTracksHandler
from application.read.handlers.album_handler import AlbumsOfAccount, AlbumsOfArtistHandler, TracksOfAlbumHandler
from application.read.handlers.media_handler import MediaHandler,MediaAlbumsHandler, MediaPlaylistsHandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


api.add_resource(PlaylistAccountHandler, '/account/<string:idAccount>/playlist')
api.add_resource(AlbumsOfArtistHandler, '/artist/<string:idArtist>/album')
api.add_resource(TracksOfAlbumHandler, '/album/<string:idAlbum>/track')
api.add_resource(PlaylistTracksHandler, '/playlist/<int:idPlaylist>/tracks')
api.add_resource(AlbumsOfAccount, '/account/<string:idAccount>/album')
api.add_resource(MediaHandler, '/media/<string:nameFile>')
api.add_resource(MediaAlbumsHandler, '/media/albums/<string:nameFile>')
api.add_resource(MediaPlaylistsHandler, '/media/playlists/<string:nameFile>')




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)