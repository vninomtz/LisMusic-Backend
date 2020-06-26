from albums.albums.domain.album import Album
from tracks.tracks.domain.exceptions import TrackInvalidException
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

    @classmethod
    def create(cls, title,duration, fileTrack):
        if not title:
            raise TrackInvalidException("Missing fields")

        newTrack = Track(str(uuid4()),title,duration,INITIAL_REPRODUCTIONS,fileTrack,False)
        return newTrack

    
    
    def addTrack_to_album(self, album:Album):
        self.album : Album = album
        album.addTrack(self)