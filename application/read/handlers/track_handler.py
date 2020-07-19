from tracks.tracks.application.use_cases.get_track import GetTrack
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from infraestructure.sqlserver_repository_album import SqlServerAlbumRepository
from tracks.tracks.domain.exceptions import DataBaseException,TrackInvalidException,TrackNotExistsException, InvalidParamsException
from flask_restful import Resource
from flask import jsonify
from tracks.tracks.application.use_cases import search_tracks, get_tracks_radio_gender, get_tracks_history_account, get_tracks_of_album
from albums.albums.domain.exceptions import AlbumNotExistsException
from albums.albums.application.use_cases import exists_album
from application.writer.handlers.login_handler import authorization_token

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

class TracksOfAlbumHandler(Resource):
    @authorization_token
    def get(self, idAlbum):
        try:
            usecase_exist_album = exists_album.ExistsAlbum(SqlServerAlbumRepository())
            dtoclass_album = exists_album.ExistsAlbumInputDto(idAlbum)
            usecase_exist_album.execute(dtoclass_album)

            usecase = get_tracks_of_album.GetTracksOfAlbum(SqlServerTrackRepository())
            dtoclass = get_tracks_of_album.GetTracksOfAlbumInputDto(idAlbum)
            list_tracks = usecase.execute(dtoclass)

            return [track.to_json_for_search() for track in list_tracks], 200
            
        except AlbumNotExistsException as ex:
            return {"error": str(ex)}, 400
        except DataBaseException as ex:
            return {"error": str(ex)}, 500

class SearchTrackHandler(Resource):
    def get(self, queryCriterion):
        try:
            usecase = search_tracks.SearchTrack(SqlServerTrackRepository())
            list_tracks = usecase.execute(queryCriterion)
            return [ob.to_json_for_search() for ob in list_tracks], 200
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

class TracksHistoryAccount(Resource):
    def get(self, idAccount):
        try:
            use_case = get_tracks_history_account.GetTracksHistoryAccount(SqlServerTrackRepository()) 
            list_tracks = use_case.execute(idAccount);
            return [ob.to_json_for_search() for ob in list_tracks], 200
        except InvalidParamsException as ex:
            return {"error": str(ex)}, 400
        except Exception as ex:
            return {"error": str(ex)}, 500
