from playlists.playlists.domain.exceptions import DataBaseException, EmptyFieldsException, PlaylistNotExistException
from playlists.playlists.application.repository.repository_playlist import PlaylistRepository

class ExistsTrackPlaylist:
    def __init__(self, repository: PlaylistRepository):
        self.repository = repository

    def execute(self, idPlaylist: int, idTrack:str):
        if not idPlaylist or not idTrack:
            raise EmptyFieldsException("Empty Fields")

        try:
            return self.repository.exists_track(idPlaylist, idTrack)
        except DataBaseException as ex:
            raise DataBaseException("Database connection error")