import sys
sys.path.append("../../")
from tracks.tracks.application.use_cases import update_track
from flask import Flask, request
from flask_restful import Resource
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.exceptions import TrackInvalidException, TrackNotExistsException
from tracks.tracks.domain.track import Track


class TrackHandler(Resource):
    def put(self):
        print('updating track')
        use_case = update_track.UpdateTrack(SqlServerTrackRepository())
        dtoclass = update_track.UpdateTrackInputDto(
            request.json["idTrack"],
            request.json["title"],
            request.json["duration"],
            request.json["reproductions"],
            request.json["fileTrack"],
            request.json["available"],
            request.json["idAlbum"]
        )
        try:
            track = use_case.execute(dtoclass)

            return track.to_json(), 200
        except TrackInvalidException as ex:
            return {"error": str(ex)}, 400
        except TrackNotExistsException as ex:
            return {"error": str(ex)}, 404
        except Exception as ex:
            return {"error": str(ex)}, 500
            
        
