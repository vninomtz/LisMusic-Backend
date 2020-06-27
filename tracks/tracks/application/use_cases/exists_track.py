from tracks.tracks.application.repositories import repositorie_track
from tracks.tracks.domain.exceptions import DataBaseException, TrackNotExistsException, TrackInvalidException
from tracks.tracks.domain.track import Track
from dataclasses import dataclass

@dataclass
class ExistsTrackInputDto:
    idTrack: str = None

class ExistsTrack:
    def __init__(self, repository: TrackRepository):
        self.repository = repository

    def execute(self, inputTrack: ExistsTrackInputDto):
        if not inputTrack.idTrack:
            raise TrackInvalidException("Empty fields")
        
        try:
            if not self.repository.exist_track(inputTrack.idTrack):
                raise TrackNotExistsException("Track not exists")
        except DataBaseException as ex:
            raise DataBaseException(ex)
        