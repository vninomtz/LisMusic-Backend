
from albums.albums.domain.exceptions import AlbumInvalidException, AlbumTypeInvalidException
import datetime
from uuid import uuid4
class Album:
    def __init__(self,idAlbum=None,title=None,cover=None,publication=None,recordCompany=None,
                idMusicGender=None,idAlbumType=None, idArtist=None):
        self.idAlbum = idAlbum
        self.title = title
        self.cover = cover
        self.publication = publication
        self.recordCompany = recordCompany
        self.idMusicGender = idMusicGender
        self.idAlbumType = idAlbumType
        self.idArtist = idArtist

    @classmethod    
    def create(cls, title,cover,publication,recordCompany,idMusicGender,idAlbumType, idArtist):
        if not cover:
            cover = "defaultAlbum.jpg"
  
        new_album = Album(str(uuid4()), title,cover,publication, recordCompany,idMusicGender,idAlbumType,idArtist)
        return new_album

    def to_json(self):
        album_to_json = {
        "idAlbum": self.idAlbum,
        "title": self.title,
        "cover": self.cover,
        "publication": self.publication,
        "recordCompany": self.recordCompany,
        "idMusicGender": self.idMusicGender,
        "idAlbumType": self.idAlbumType,
        "idArtist": self.idArtist,
    }
        return album_to_json