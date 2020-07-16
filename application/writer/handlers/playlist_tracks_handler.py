from playlists.playlists.domain.exceptions import DataBaseException, PlaylistInvalidException, PlaylistNotExistException, EmptyFieldsException
from playlists.playlists.application.use_cases import exists_playlist, exists_track_playlist, add_track_to_playlist, remove_track_to_playlist
from infraestructure.sqlserver_repository_playlist import SqlServerPlaylistRepository
from flask import Flask, request
from flask_restful import Resource

class PlaylistTracksHandler(Resource):
    def post(self, idPlaylist, idTrack):
        exists_usecase = exists_playlist.ExistsPlaylist(SqlServerPlaylistRepository())
        exists_track_usecase = exists_track_playlist.ExistsTrackPlaylist(SqlServerPlaylistRepository())
        add_usecase = add_track_to_playlist.AddTrackPlaylist(SqlServerPlaylistRepository())
        try:
            if exists_usecase.execute(idPlaylist):
                if exists_track_usecase.execute(idPlaylist, idTrack):
                    return {"error": "Track already exists in playlist"}, 400
                else:
                    if add_usecase.execute(idPlaylist, idTrack):
                        return {}, 201
        except EmptyFieldsException as ex:
            return {"error": str(ex)}, 400
        except PlaylistNotExistException as ex:
            return {"error": str(ex)}, 404
        except DataBaseException as ex:
            return {"error": str(ex)}, 500
        pass

    def delete(self, idPlaylist, idTrack):
        exists_usecase = exists_playlist.ExistsPlaylist(SqlServerPlaylistRepository())
        exists_track_usecase = exists_track_playlist.ExistsTrackPlaylist(SqlServerPlaylistRepository())
        remove_usecase = remove_track_to_playlist.RemoveTrackPlaylist(SqlServerPlaylistRepository())
        try:
            if exists_usecase.execute(idPlaylist):
                if not exists_track_usecase.execute(idPlaylist, idTrack):
                    return {"error": "Track not exists in playlist"}, 404
                else:
                    if remove_usecase.execute(idPlaylist, idTrack):
                        return {}, 200
        except EmptyFieldsException as ex:
            return {"error": str(ex)}, 400
        except PlaylistNotExistException as ex:
            return {"error": str(ex)}, 404
        except DataBaseException as ex:
            return {"error": str(ex)}, 500
        pass