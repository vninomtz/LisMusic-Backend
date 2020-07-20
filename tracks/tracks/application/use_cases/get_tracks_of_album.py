from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from albums.albums.domain.album import Album
from tracks.tracks.domain.track import Track
from tracks.tracks.domain.exceptions import TrackInvalidException, DataBaseException
from dataclasses import dataclass

@dataclass
class GetTracksOfAlbumInputDto:
    idAlbum:str = None

class GetTracksOfAlbum:
    def __init__(self, repository: TrackRepository):
        self.repository: TrackRepository = repository

    def execute(self, inputAlbum:GetTracksOfAlbumInputDto):
        try:
            list_tracks = self.repository.get_tracks_of_album(inputAlbum.idAlbum)
            return list_tracks
        except DataBaseException as ex:
            raise DataBaseException(ex)
