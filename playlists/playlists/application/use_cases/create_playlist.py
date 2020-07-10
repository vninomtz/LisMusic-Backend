from infraestructure.sqlserver_repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from playlists.playlists.domain.exceptions import DataBaseException, PlaylistInvalidException
from dataclasses import dataclass

@dataclass
class CreatePlaylistInputDto:
    title: str = None
    cover: str = None
    publicPlaylist: str = None
    idPlaylistType: str = None
    idAccount: str = None

class CreatePlaylist:
        def __init__(self, repository: PlaylistRepository):
            self.repository = repository

        def execute(self, inputPlaylist: CreatePlaylistInputDto):
            new_playlist = Playlist.create(inputPlaylist.title, inputPlaylist.cover, inputPlaylist.publicPlaylist, inputPlaylist.idPlaylistType, inputPlaylist.idAccount)

            if not inputPlaylist.title or not inputPlaylist.cover or not inputPlaylist.publicPlaylist or not inputPlaylist.idPlaylistType:
                raise PlaylistInvalidException
          #  print("id" + .idAccount)

            new_playlist.account.idAccount = inputPlaylist.idAccount

            try:
                
                self.repository.save(new_playlist)
                return new_playlist
            except DataBaseException as ex:
                raise ex("Database connection error")
        


        
    