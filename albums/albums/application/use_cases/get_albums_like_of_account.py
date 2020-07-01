from albums.albums.application.repositories.repository_album import AlbumRepository
from artists.artists.application.repositories.repository_artist import ArtistRepository
from albums.albums.domain.album import Album
from artists.artists.domain.exceptions import ArtistInvalidException, DataBaseException
from artists.artists.application.use_cases import exists_artist
from dataclasses import dataclass
import json

@dataclass
class GetAlbumsLikeOfAccountInputDto:
    idAlbum: str = None

class GetAlbumsLikeOfAccount:
    def __init__(self, album_repository: AlbumRepository):
        self.album_repository = album_repository
       
    def execute(self, inputAlbum: GetAlbumsLikeOfAccountInputDto):
        try:
            list_albums = self.album_repository.get_albums_like_of_account(inputAlbum.idAlbum)
            return list_albums
        except DataBaseException as ex:
            raise DataBaseException(ex)