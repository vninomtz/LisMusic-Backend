from albums.albums.application.repositories.repository_album import AlbumRepository
from albums.albums.domain.album import Album
from albums.albums.domain.exceptions import DataBaseException, AlbumNotExistsException, AlbumInvalidException
from dataclasses import dataclass
import datetime
@dataclass
class UpdateAlbumInputDto:
    idAlbum: str = None
    title: str = None
    cover: str = None
    publication: datetime.date = None
    recordCompany: str = None
    idMusicGender: int = None
    idAlbumType: int = None
    tracks: [] = None
    
class UpdateAlbum:
    def __init__(self, repository: AlbumRepository):
        self.repository = repository

    def execute(self, inputAlbum: UpdateAlbumInputDto):

        if not inputAlbum.idAlbum:
            raise AlbumInvalidException("Empty ID field")

        if not self.repository.exist_album(inputAlbum.idAlbum):
            raise AlbumNotExistsException("Album not exists")

        album = Album(inputAlbum.idAlbum, inputAlbum.title, inputAlbum.cover, inputAlbum.publication, 
                    inputAlbum.description, inputAlbum.idMusicGender,inputAlbum.idAlbumType,inputAlbum.tracks) 
        try:
            result = self.repository.update(album)
            return result
        except DataBaseException:
            raise DataBaseException("Database connection error")