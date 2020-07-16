from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.exceptions import DataBaseException, EmptyFieldsException

class DeletePlaylist:
    def __init__(self, repository: PlaylistRepository):
        self.repository = repository

    def execute(self, idPlaylist: int):
        if not idPlaylist:
            raise EmptyFieldsException("Empty Fields")

        try:
            if self.repository.delete(idPlaylist):
                return True
        except DataBaseException as ex:
            raise DataBaseException("Database connection error")
        