from playlists.playlists.application.use_cases import create_playlist, exists_playlist, delete_playlist
from infraestructure.sqlserver_repository_playlist import SqlServerPlaylistRepository
from flask import Flask, request
from flask_restful import Resource
from playlists.playlists.domain.exceptions import DataBaseException, PlaylistInvalidException, PlaylistNotExistException, EmptyFieldsException
from flask.json import jsonify

class PlaylistHandler(Resource):
    def post(self, idPlaylist):
        usecase = create_playlist.CreatePlaylist(SqlServerPlaylistRepository())
        dtoclass = create_playlist.CreatePlaylistInputDto(
            request.json["title"],
            request.json["cover"],
            request.json["publicPlaylist"],
            request.json["idPlaylistType"],
            request.json["idAccount"],
        )
 
        try:
            playlist = usecase.execute(dtoclass) 
            return playlist.to_json_create(), 200
        except PlaylistInvalidException as ex:
            return {"error": str(ex)}, 404
        except DataBaseException as ex:
            return {"error": str(ex)}, 500

    def delete(self, idPlaylist):
        exists_usecase = exists_playlist.ExistsPlaylist(SqlServerPlaylistRepository())
        delete_usecase = delete_playlist.DeletePlaylist(SqlServerPlaylistRepository())
        try:
            if exists_usecase.execute(idPlaylist):
                if delete_usecase.execute(idPlaylist):
                    return {}, 200
        except EmptyFieldsException as ex:
            return {"error": str(ex)}, 400
        except PlaylistNotExistException as ex:
            return {"error": str(ex)}, 404
        except DataBaseException as ex:
            return {"error": str(ex)}, 500

        