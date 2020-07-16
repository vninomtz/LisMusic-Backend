from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.track import Track
from dataclasses import dataclass
from tracks.tracks.domain.exceptions import TrackInvalidException, TrackNotExistsException
from dataclasses import dataclass

@dataclass
class UpdateTrackInputDto:
    idTrack: str = None
    title: str = None
    duration: str = None
    reproductions: int = None
    fileTrack: str = None
    available: bool = None
    idAlbum: str = None
    
class UpdateTrack:
    def __init__(self, repository: TrackRepository):
        self.repository = repository

    def execute(self, trackInput: UpdateTrackInputDto):

        if not trackInput.idTrack:
            raise TrackInvalidException("Empty ID field")
        
        if not self.repository.exists_track(trackInput.idTrack):
            raise TrackNotExistsException("Track not exists")

        track = Track(idTrack=trackInput.idTrack,title=trackInput.title,duration=trackInput.duration,
        reproductions=trackInput.reproductions,fileTrack=trackInput.fileTrack,avaible=trackInput.available)
        track.album.idAlbum = trackInput.idAlbum

        try:
            self.repository.update(track)
            return track
        except Exception as ex:
            return ex

        
