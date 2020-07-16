import abc 
from playlists.playlists.domain.playlist import Playlist

class PlaylistRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, playlist: Playlist):
        pass

    @abc.abstractmethod
    def update(self, playlist: Playlist):
        pass

    @abc.abstractmethod
    def delete(self, playlistId: int):
        pass

    @abc.abstractmethod
    def exists_playlist(self, playlistId: int):
        pass

    @abc.abstractmethod
    def get_playlist_of_account(self, idAccount:str):
        pass

    @abc.abstractmethod
    def add_track(self, idPlaylist:int, idTrack:str):
        pass

    @abc.abstractmethod
    def remove_track(self, idPlaylist:int, idTrack:str):
        pass

    @abc.abstractmethod
    def exists_track(self, idPlaylist:int, idTrack:str):
        pass
    