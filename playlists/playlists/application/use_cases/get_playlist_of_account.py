from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from playlists.playlists.domain.exceptions import EmptyFieldsException, DataBaseException
from accounts.accounts.application.use_cases.exists_account import ExistAccount
from accounts.accounts.domain.exceptions import AccountNotExistException
from infraestructure.sqlserver_repository import SqlServerAccountRepository
import json

class GetPlaylistForAccount:
    def __init__(self, repository):
        self.repository: PlaylistRepository = repository

    def execute(self, idAccount:str):
        if not idAccount:
            raise EmptyFieldsException("Missing fields")

        usecase = ExistAccount(SqlServerAccountRepository())
        
        if not usecase.execute(idAccount):
            raise AccountNotExistException("Account not exist")

        try:
            listPlaylist = self.repository.get_playlist_of_account(idAccount)
            if listPlaylist != []:
                return listPlaylist
            else:
                return ""
        except DataBaseException as ex:
            raise DataBaseException(ex)

    def create_json_response(self, listPlaylist):
        return json.dumps([ob.to_json() for ob in listPlaylist])
