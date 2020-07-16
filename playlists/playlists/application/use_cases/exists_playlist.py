from playlists.playlists.domain.exceptions import DataBaseException, EmptyFieldsException, PlaylistNotExistException
from playlists.playlists.application.repository.repository_playlist import PlaylistRepository

class ExistsPlaylist:
    def __init__(self, repository: PlaylistRepository):
        self.repository = repository

    def execute(self, idPlaylist: int):
        if not idPlaylist:
            raise EmptyFieldsException("Empty Fields")

        try:
            if not self.repository.exists_playlist(idPlaylist):
                raise PlaylistNotExistException("Playlist not exists")
            else:
                return True
        except DataBaseException as ex:
            raise DataBaseException("Database connection error")