from albums.albums.application.repositories.repository_album import AlbumRepository
from albums.albums.domain.exceptions import DataBaseException, AlbumNotExistsException, AlbumInvalidException
from albums.albums.domain.album import Album
from dataclasses import dataclass


@dataclass
class DeleteAlbumInputDto:
    idAlbum: str = None


class DeleteAlbum:
    def __init__(self, repository: AlbumRepository):
        self.repository = repository

    def execute(self, inputAlbum: DeleteAlbumInputDto):
        if not inputAlbum.idAlbum:
            raise AlbumInvalidException("Empty fields")

        if not self.repository.exists_album(inputAlbum.idAlbum):
            raise AlbumNotExistsException("Album not exists")
        
        try:
            result = self.repository.delete(inputAlbum.idAlbum)
            return result
        except DataBaseException as ex:
            raise DataBaseException(ex)