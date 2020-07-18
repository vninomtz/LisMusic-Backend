from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.exceptions import InvalidParamsException, DataBaseException
from tracks.tracks.domain.track import Track


class GetTracksHistoryAccount():
    def __init__(self, repository):
        self.repository:TrackRepository = repository

    def execute(self, idAccount:int):
        if not idAccount:
            raise InvalidParamsException("Invalid params")

        try:
            list_tracks = self.repository.get_tracks_account_history(idAccount)
            return list_tracks
        except DataBaseException as ex:
            raise DataBaseException(ex)

