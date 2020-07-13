
from albums.albums.domain.exceptions import AlbumInvalidException, AlbumTypeInvalidException
from artists.artists.domain.artist import Artist
import datetime
from uuid import uuid4
class Album:
    def __init__(self,idAlbum=None,title=None,cover=None,publication=None,recordCompany=None,
                idMusicGender=None,idAlbumType=None, artistName=None):
        self.idAlbum = idAlbum
        self.title = title
        self.cover = cover
        self.publication = publication
        self.recordCompany = recordCompany
        self.idMusicGender = idMusicGender
        self.idAlbumType = idAlbumType
        self.artist = Artist()
        self.artist.name = artistName

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
        "cover": 'http://10.0.2.2:6000/media/albums/{}'.format(self.cover),
        "publication": self.publication,
        "recordCompany": self.recordCompany,
        "idMusicGender": self.idMusicGender,
        "idAlbumType": self.idAlbumType,
        "artistName": self.artist.name
    }
        return album_to_json