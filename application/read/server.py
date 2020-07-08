import sys
sys.path.append("../../")
from application.read.handlers.playlist_handler import PlaylistAccountHandler, PlaylistTracksHandler
from application.read.handlers.album_handler import AlbumsLikeOfAccountHandler, AlbumsOfArtistHandler, TracksOfAlbumHandler
from application.read.handlers.media_handler import MediaAlbumsHandler, MediaArtistsHandler, MediaHandler, MediaPlaylistsHandler
from application.read.handlers.artist_handler import ArtistsLikeOfAccountHandler
from application.read.handlers.track_handler import TrackHandler
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


api.add_resource(PlaylistAccountHandler, '/account/<string:idAccount>/playlist')
api.add_resource(AlbumsOfArtistHandler, '/artist/<string:idArtist>/album')
api.add_resource(TracksOfAlbumHandler, '/album/<string:idAlbum>/track')
api.add_resource(PlaylistTracksHandler, '/playlist/<int:idPlaylist>/tracks')
api.add_resource(AlbumsLikeOfAccountHandler, '/account/<string:idAccount>/albumsLike')
api.add_resource(MediaHandler, '/media/<string:nameFile>')
api.add_resource(MediaAlbumsHandler, '/media/albums/<string:nameFile>')
api.add_resource(MediaPlaylistsHandler, '/media/playlists/<string:nameFile>')
api.add_resource(MediaArtistsHandler, '/media/artists/<string:fileName>')
api.add_resource(ArtistsLikeOfAccountHandler, '/account/<string:idAccount>/artistsLike')
api.add_resource(TrackHandler, '/track/<string:idTrack>')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)