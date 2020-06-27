from albums.albums.application.repositories.repository_album import AlbumRepository
from artists.artists.application.repositories.repository_artist import ArtistRepository
from albums.albums.domain.album import Album
from artists.artists.domain.exceptions import ArtistInvalidException, DataBaseException
from artists.artists.application.use_cases import exists_artist
from dataclasses import dataclass
import json

@dataclass
class GetAlbumsByIdArtistInputDto:
    idArtist: str = None

class GetAlbumsByIdArtist:
    def __init__(self, album_repository: AlbumRepository, artist_repository: ArtistRepository):
        self.album_repository = album_repository
        self.artist_repository = artist_repository

    def execute(self, inputIdArtist: GetAlbumsByIdArtistInputDto):
        usecase_exists_artist = exists_artist.ExistsArtist(self.artist_repository)
        dtoclass = exists_artist.ExistsArtistInputDto(inputIdArtist.idArtist)
        usecase_exists_artist.execute(dtoclass)
        
        try:
            list_albums = self.album_repository.get_albums_by_id_artist(inputIdArtist.idArtist)
            return list_albums
        except DataBaseException as ex:
            raise DataBaseException(ex)