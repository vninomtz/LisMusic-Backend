from infraestructure.sqlserver_repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from playlists.playlists.domain.exceptions import DataBaseException, PlaylistInvalidException
import datetime
from utils.Image import Image
from dataclasses import dataclass

@dataclass
class UpdatePlaylistInputDto:
    idPlaylist:int = None
    title: str = None
    cover: str = None
    publicPlaylist: bool = None
    idAccount:str = None

class UpdatePlaylist:
        def __init__(self, repository: PlaylistRepository):
            self.repository = repository

        def execute(self, inputPlaylist: UpdatePlaylistInputDto):
            if not inputPlaylist.idPlaylist:
                raise PlaylistInvalidException("Empty Fields ")

            if inputPlaylist.cover:
                nameCover = Image.generate_name(inputPlaylist.idAccount)
                if Image.save_image(inputPlaylist.cover, nameCover, "Playlist"):
                    inputPlaylist.cover = nameCover
            else:
                inputPlaylist.cover = None
                
            playlist = Playlist(inputPlaylist.idPlaylist,inputPlaylist.title,None,
                                inputPlaylist.cover,inputPlaylist.publicPlaylist,None)
            try:
                if self.repository.update(playlist):
                    return True
            except DataBaseException as ex:
                raise ex("Database connection error")
        


        
    