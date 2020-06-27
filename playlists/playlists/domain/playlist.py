from playlists.playlists.domain.exceptions import InvalidPlaylistException
import datetime

class Playlist:
    def __init__(self, idPlaylist=None, title=None, creation=None, cover=None, publicPlaylist=None,
                    idPlaylistType=None, idAccount=None):
        self.idPlaylist: int = idPlaylist
        self.title: str = title
        self.creation: datetime.date = creation
        self.cover: str = cover
        self.publicPlaylist: bool = publicPlaylist
        self.idPlaylistType: int = idPlaylistType
        self.idAccount = idAccount

    @classmethod
    def create(cls, title, cover, publicPlaylist, idPlaylistType, idAccount):
        if not title or not idAccount or not idPlaylistType:
            raise InvalidPlaylistException("Missing fields")

        if not cover:
            cover = "defaultPlaylistCover.jpg"

        newPlaylist = Playlist(None, title, datetime.datetime.now(),cover,publicPlaylist, idPlaylistType, idAccount)

        return newPlaylist

    def to_json(self):
        playlist_to_json = {
            "idPlaylist":self.idPlaylist,
            "title":self.title,
            "creation": str(self.creation),
            "cover":self.cover,
            "publicPlaylist":self.publicPlaylist,
            "idPlaylistType":self.idPlaylistType,
            "idAccount":self.idAccount
        }
        return playlist_to_json
        
