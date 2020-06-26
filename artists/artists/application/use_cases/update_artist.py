from artists.artists.application.repositories.repository_artist import ArtistRepository
from artists.artists.domain.artist import Artist
from artists.artists.domain.exceptions import DataBaseException, ArtistNotExistsException, ArtistInvalidException
from dataclasses import dataclass
import datetime
@dataclass
class UpdateArtistInputDto:
    idArtist: str = None
    name: str = None
    cover: str = None
    description: str = None
    
class UpdateArtist:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository

    def execute(self, inputArtist: UpdateArtistInputDto):

        if not inputArtist.idArtist:
            raise ArtistInvalidException("Empty ID field")

        if not self.repository.exist_artist(inputArtist.idArtist):
            raise ArtistNotExistsException("Artist not exists")

        artist = Artist(inputArtist.idArtist, inputArtist.name, inputArtist.cover, None, inputArtist.description)
        try:
            result = self.repository.update(artist)
            return result
        except DataBaseException:
            raise DataBaseException("Database connection error")
        
