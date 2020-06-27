from playlists.playlists.application.use_cases.get_playlist_of_account import GetPlaylistForAccount
from playlists.playlists.domain.exceptions import DataBaseException,EmptyFieldsException
from accounts.accounts.domain.exceptions import AccountNotExistException
from infraestructure.sqlserver_repository_playlist import PlaylistRepository
from flask_restful import Resource, abort
from flask import jsonify

class PlaylistAccountHandler(Resource):
    def get(self, idAccount):
        usecase = GetPlaylistForAccount(PlaylistRepository())
        try:
            playlits = usecase.execute(idAccount)
            return jsonify([ob.to_json() for ob in playlits])
        except EmptyFieldsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except AccountNotExistException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except DataBaseException:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response
        
        