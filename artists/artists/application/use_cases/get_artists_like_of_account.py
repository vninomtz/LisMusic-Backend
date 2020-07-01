
from artists.artists.application.repositories.repository_artist import ArtistRepository
from albums.albums.domain.album import Album
from artists.artists.domain.exceptions import ArtistInvalidException, DataBaseException
from artists.artists.application.use_cases import exists_artist
from dataclasses import dataclass
import json

@dataclass
class GetArtistsLikeOfAccountInputDto:
    idArtist: str = None

class GetArtistsLikeOfAccount:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository
       
    def execute(self, inputArtist: GetArtistsLikeOfAccountInputDto):
        try:
            list_artists = self.repository.get_artists_like_of_account(inputArtist.idArtist)
            return list_artists
        except DataBaseException as ex:
            raise DataBaseException(ex)