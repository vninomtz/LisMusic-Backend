from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.exceptions import DataBaseException, TrackNotExistsException, TrackInvalidException
import datetime

class AddTrackPlayed:
    def __init__(self, repository: TrackRepository):
        self.repository = repository

    def execute(self, idTrack:str, idAccount:str):
        if not idTrack or not idAccount:
            raise TrackInvalidException("Empty fields")

        if not self.repository.exists_track(idTrack):
            raise TrackNotExistsException("Track not exists")
        try:
            print(datetime.datetime.now())
            result = self.repository.add_track_played(idTrack,datetime.datetime.now().isoformat(),idAccount)
            
            return result
        except DataBaseException as ex:
            raise DataBaseException(ex)
