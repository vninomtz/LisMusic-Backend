from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.exceptions import DataBaseException, EmptyFieldsException

class RemoveTrackPlaylist:
    def __init__(self, repository: PlaylistRepository):
        self.repository = repository

    def execute(self, idPlaylist: int, idTrack:str):
        if not idPlaylist or not idTrack:
            raise EmptyFieldsException("Empty Fields")

        try:
            if self.repository.remove_track(idPlaylist,idTrack):
                return True
        except DataBaseException as ex:
            raise DataBaseException("Database connection error")
        