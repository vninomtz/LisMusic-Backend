import sys
sys.path.append("../../")
from application.read.handlers.playlist_handler import PlaylistAccountHandler, PlaylistTracksHandler, SearchPlaylistHandler
from application.read.handlers.album_handler import AlbumsLikeOfAccountHandler, AlbumsOfArtistHandler, SearchAlbumHandler
from application.read.handlers.media_handler import MediaAlbumsHandler, MediaArtistsHandler, MediaHandler, MediaPlaylistsHandler
from application.read.handlers.artist_handler import ArtistsLikeOfAccountHandler, SearchArtistHandler, ArtistAccount
from application.read.handlers.track_handler import SearchTrackHandler, TrackHandler, TracksRadioHandler, TracksHistoryAccount, TracksOfAlbumHandler
from application.read.handlers.personal_tracks_handler import PersonalTracksAccountHandler
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
api.add_resource(SearchArtistHandler, '/artists/<string:queryCriterion>')
api.add_resource(SearchAlbumHandler, '/albums/<string:queryCriterion>')
api.add_resource(SearchTrackHandler, '/tracks/<string:queryCriterion>')
api.add_resource(SearchPlaylistHandler, '/playlists/<string:queryCriterion>')
api.add_resource(TracksRadioHandler, "/radio/gender/<int:idMusicGender>")
api.add_resource(TracksHistoryAccount,'/account/<string:idAccount>/tracksHistory')
api.add_resource(PersonalTracksAccountHandler, '/account/<string:idAccount>/personalTracks')
api.add_resource(ArtistAccount, '/account/<string:idAccount>/artist')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6000,debug=True)