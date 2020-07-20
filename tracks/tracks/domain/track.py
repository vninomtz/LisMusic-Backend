from albums.albums.domain.album import Album
from tracks.tracks.domain.exceptions import TrackInvalidException
from musicgenders.genders.domain.musicgender import MusicGender
from uuid import uuid4

INITIAL_REPRODUCTIONS = 0

class Track:
    def __init__(self=None,idTrack=None,title=None,duration=None,reproductions=None,fileTrack=None,avaible=None):
        self.idTrack: str = idTrack
        self.title: str = title
        self.duration: float = duration
        self.reproductions: int = reproductions
        self.fileTrack: str = fileTrack
        self.avaible: bool = avaible
        self.album: Album = Album()
   
        

    @classmethod
    def create(cls, title,duration, fileTrack):
        if not title:
            raise TrackInvalidException("Missing fields")

        newTrack = Track(str(uuid4()),title,duration,INITIAL_REPRODUCTIONS,fileTrack,False)
        return newTrack

    def addTrack_to_album(self, album:Album):
        self.album : Album = album

    def to_json(self):
        track_to_json = {
            "idTrack": self.idTrack,
            "title": self.title,
            "duration": self.duration,
            "reproductions": self.reproductions,
            "fileTrack": self.fileTrack,
            "avaible": self.avaible
        }
        return track_to_json;
    
    def to_json_for_playlist(self):
        track_to_json = {
            "idTrack": self.idTrack,
            "title": self.title,
            "duration": self.duration,
            "fileTrack": self.fileTrack,
            "avaible": self.avaible,
            "cover": 'http://10.0.2.2:6000/media/albums/{}'.format(self.album.cover),
            "artistName": self.album.artist.name,
            "album_uri": 'http://10.0.2.2:6000/album/{}'.format(self.album.idAlbum),
            "artist_uri": 'http://10.0.2.2:6000/artist/{}'.format(self.album.artist.idArtist),
            "Album": self.album.to_json()
        }
        return track_to_json;


    def to_json_for_search(self):
        track_to_json = {
            "idTrack": self.idTrack,
            "title": self.title,
            "duration": self.duration,
            "reproductions": self.reproductions,
            "fileTrack": self.fileTrack,
            "avaible": self.avaible,
            "artistName": self.album.artist.name,
            "Album": self.album.to_json()
            
        }
        return track_to_json;

    def to_json_for_radio(self):
        track_to_json = {
            "idTrack": self.idTrack,
            "title": self.title,
            "duration": self.duration,
            "fileTrack": self.fileTrack,
            "avaible": self.avaible,
            "Album": self.album.to_json()
            
        }
        return track_to_json;