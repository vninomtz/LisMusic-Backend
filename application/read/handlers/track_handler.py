from tracks.tracks.application.use_cases.get_track import GetTrack
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.exceptions import DataBaseException,TrackInvalidException,TrackNotExistsException
from flask_restful import Resource
from flask import jsonify


class TrackHandler(Resource):
    def get(self, idTrack):
        usecase = GetTrack(SqlServerTrackRepository())
        try:
            track = usecase.execute(idTrack)
            return track.to_json()
        except TrackInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except TrackNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response