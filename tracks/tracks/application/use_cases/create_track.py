from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from albums.albums.domain.album import Album
from tracks.tracks.domain.track import Track
from tracks.tracks.domain.exceptions import TrackInvalidException, DataBaseException

@dataclass
class CreateTrackInputDto:
    title:str = None
    duration:float = None
    fileTrack:str = None
    album: Album = None
class CreateTrack:
    def __init__(self, repository: TrackRepository):
        self.repository: TrackRepository = repository

    def execute(self, inputTrack:CreateTrackInputDto):
        try:
            newTrack = Track.create(inputTrack.title,inputTrack.duration,inputTrack.fileTrack)
            newTrack.addTrack_to_album(inputTrack.album)
        except TrackInvalidException as ex:
            raise TrackInvalidException(ex)
        
        try:
            if self.repository.save(newTrack):
               return newTrack
            else:
                return None
        except DataBaseException as ex:
            raise DataBaseException(ex)
