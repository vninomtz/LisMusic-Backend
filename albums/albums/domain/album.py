from tracks.tracks.domain.track import Track
from albums.albums.domain.exceptions import AlbumInvalidException, AlbumTypeInvalidException
from albums.albums.domain.album_types import AlbumTypes
import datetime
from uuid import uuid4


class Album:
    def __init__(self):
        self.idAlbum: str
        self.title: str
        self.cover: str
        self.publication: datetime.date
        self.recordCompany: str
        self.idMusicGender: int
        self.idAlbumType: int
        self.tracks: Track = []

    @classmethod    
    def create(cls, title,cover,publication,recordCompany,musicGender,albumType):
        if not title or not recordCompany or not albumType:
            raise AlbumInvalidException("Missing fields")
        if not cover:
            cover = "defaultAlbum.jpg"
        try:
            idAlbumType = AlbumTypes[albumType]
        except Exception:
            raise AlbumTypeInvalidException("Incorrect album type")
        newAlbum = Album(str(uuid4()), title,cover,publication, recordCompany,musicGender, idAlbumType.value)

        return newAlbum


    def addTrack(self, track: Track):
        self.tracks.append(track)