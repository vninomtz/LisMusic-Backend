from tracks.tracks.application.use_cases.get_track import GetTrack
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.exceptions import DataBaseException,TrackInvalidException,TrackNotExistsException, InvalidParamsException
from flask_restful import Resource
from flask import jsonify
from tracks.tracks.application.use_cases import search_tracks, get_tracks_radio_gender


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

class SearchTrackHandler(Resource):
    def get(self, queryCriterion):
        try:
            usecase = search_tracks.SearchTrack(SqlServerTrackRepository())
            list_artists = usecase.execute(queryCriterion)
            return [ob.to_json_for_search() for ob in list_artists], 200
        except TrackInvalidException as ex:
            return {"error": str(ex)}, 400
        except TrackNotExistsException as ex:
            return {"error": str(ex)}, 400
        except Exception as ex:
            return {"error": str(ex)}, 500


class TracksRadioHandler(Resource):
    def get(self, idMusicGender):
        try:
            usecase = get_tracks_radio_gender.GetTracksRadioGender(SqlServerTrackRepository())
            list_tracks = usecase.execute(idMusicGender)
            return [ob.to_json_for_radio() for ob in list_tracks], 200
        except InvalidParamsException as ex:
            return {"error": str(ex)}, 400
        except Exception as ex:
            return {"error": str(ex)}, 500




