from albums.albums.application.repositories.repository_album import AlbumRepository
from albums.albums.domain.exceptions import DataBaseException, AlbumNotExistsException, AlbumInvalidException
from albums.albums.domain.album import Album
from dataclasses import dataclass

@dataclass
class ExistsAlbumInputDto:
    idAlbum: str = None

class ExistsAlbum:
    def __init__(self, repository: AlbumRepository):
        self.repository = repository

    def execute(self, inputAlbum: ExistsAlbumInputDto):
        if not inputAlbum.idAlbum:
            raise AlbumInvalidException("Empty fields")
        
        try:
            if not self.repository.exists_album(inputAlbum.idAlbum):
                raise AlbumNotExistsException("Album not exists")
        except DataBaseException as ex:
            raise DataBaseException(ex)
        