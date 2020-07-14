from playlists.playlists.application.use_cases import create_playlist
from infraestructure.sqlserver_repository_playlist import SqlServerPlaylistRepository
from flask import Flask, request
from flask_restful import Resource
from playlists.playlists.domain.exceptions import DataBaseException, PlaylistInvalidException
from flask.json import jsonify

class PlaylistHandler(Resource):
    def post(self):
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

        