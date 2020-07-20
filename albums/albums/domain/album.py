
from albums.albums.domain.exceptions import AlbumInvalidException, AlbumTypeInvalidException
from artists.artists.domain.artist import Artist
from musicgenders.genders.domain.musicgender import MusicGender
import datetime
from uuid import uuid4
class Album:
    def __init__(self,idAlbum=None,title=None,cover=None,publication=None,recordCompany=None,idAlbumType=None):
        self.idAlbum = idAlbum
        self.title = title
        self.cover = cover
        self.publication:datetime.date = publication
        self.recordCompany = recordCompany
        self.idAlbumType = idAlbumType
        self.artist = Artist()
        self.musicGender = MusicGender()
        self.tracks = []


    @classmethod    
    def create(cls, title,cover,publication,recordCompany,idAlbumType):
        if not cover:
            cover = "defaultAlbum.jpg"
  
        new_album = Album(str(uuid4()), title,cover,publication, recordCompany,idAlbumType)
        return new_album

    def to_json(self):
        album_to_json = {
        "idAlbum": self.idAlbum,
        "title": self.title,
        "cover": 'http://10.0.2.2:6000/media/albums/{}'.format(self.cover),
        "publication": self.publication.strftime('%Y-%m-%d') ,
        "recordCompany": self.recordCompany,
        "idAlbumType": self.idAlbumType,
        "MusicGender": self.musicGender.to_json(),
        "Artist": self.artist.to_json()

    }
        return album_to_json

    def to_json_tracks(self):
        album_to_json = {
        "idAlbum": self.idAlbum,
        "title": self.title,
        "cover": 'http://10.0.2.2:6000/media/albums/{}'.format(self.cover),
        "publication": self.publication ,
        "recordCompany": self.recordCompany,
        "idAlbumType": self.idAlbumType,
        "idMusicGender": self.musicGender.idMusicGender,
        "idArtist": self.artist.idArtist,
        "tracks": [track.to_json() for track in self.tracks]
    }
        return album_to_json