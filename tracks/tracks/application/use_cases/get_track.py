from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.exceptions import DataBaseException, TrackNotExistsException, TrackInvalidException

class GetTrack:
    def __init__(self, repository: TrackRepository):
        self.repository = repository

    def execute(self, idTrack:str):
        if not idTrack:
            raise TrackInvalidException("Empty fields")

        try:
            if not self.repository.exists_track(idTrack):
                raise TrackNotExistsException("Track not exists")

            track = self.repository.get_track(idTrack)
            return track
        except DataBaseException as ex:
            raise DataBaseException(ex)
