from infraestructure.sqlserver_repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from playlists.playlists.domain.exceptions import DataBaseException, PlaylistInvalidException
import datetime
from utils import Image
from dataclasses import dataclass

@dataclass
class CreatePlaylistInputDto:
    title: str = None
    cover: str = None
    publicPlaylist: bool = None
    idPlaylistType: str = None
    idAccount: str = None

class CreatePlaylist:
        def __init__(self, repository: PlaylistRepository):
            self.repository = repository

        def execute(self, inputPlaylist: CreatePlaylistInputDto):
            if not inputPlaylist.title or not inputPlaylist.idPlaylistType:
                raise PlaylistInvalidException("Empty Fields ")

            if inputPlaylist.cover:
                nameCover = self.generate_name(inputPlaylist.title)
                if Image.Image.save_image(inputPlaylist.cover, nameCover, "Playlist"):
                    inputPlaylist.cover = nameCover
            else:
                inputPlaylist.cover = "defaultPlaylistCover.jpeg"

            new_playlist = Playlist.create(inputPlaylist.title, inputPlaylist.cover, inputPlaylist.publicPlaylist, inputPlaylist.idPlaylistType, inputPlaylist.idAccount)

            new_playlist.account.idAccount = inputPlaylist.idAccount

            try:
                
                self.repository.save(new_playlist)
                return new_playlist
            except DataBaseException as ex:
                raise ex("Database connection error")

        def generate_name(self, title:str):
            newTitle = title.replace(" ", "")
            date = datetime.date.today()
            return "{0}_{1}.{2}".format(str(date), newTitle, "png")
        


        
    