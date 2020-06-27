from artists.artists.application.repositories.repository_artist import ArtistRepository
from artists.artists.domain.exceptions import DataBaseException, ArtistNotExistsException, ArtistInvalidException
from artists.artists.domain.artist import Artist
from dataclasses import dataclass


@dataclass
class ExistsArtistInputDto:
    idArtist: str = None


class ExistsArtist:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository

    def execute(self, inputArtist: ExistsArtistInputDto):
        if not inputArtist.idArtist:
            raise ArtistInvalidException("Empty fields")
        
        try:
            if not self.repository.exist_artist(inputArtist.idArtist):
                raise ArtistNotExistsException("Artist not exists")
        except DataBaseException as ex:
            raise DataBaseException(ex)
        