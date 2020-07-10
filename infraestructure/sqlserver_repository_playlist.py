from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from infraestructure.connection import ConnectionSQL
from playlists.playlists.domain.exceptions import DataBaseException

class SqlServerPlaylistRepository(PlaylistRepository):
    def __init__(self):
        self.connection = ConnectionSQL()
    
    def save(self, playlist: Playlist):
        self.connection.open()

        print(playlist.account.idAccount)
        sql = """\
        DECLARE @return_value int,
                @estado int,
                @salida nvarchar(1000)

        EXEC	@return_value = [dbo].[SPI_CreatePlaylist]
                @title = ?,
                @creation = ?,
                @cover = ?,
                @publicPlaylist = ?,
                @idPlaylistType = ?,
                @idAccount = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """
        
        try:
            self.connection.cursor.execute(sql, playlist.title, playlist.creation, playlist.cover,playlist.publicPlaylist,playlist.idPlaylistType, playlist.account.idAccount)

            self.connection.save()
            self.connection.close()
            
            return True
        except DataBaseException as ex:
            raise DataBaseException("Database connection error")
    

    
    def update(self, playlist: Playlist):
        pass

    
    def delete(self, playlistId: int):
        pass

    
    def exists_playlist(self, playlistId: int):
        pass

    
    def get_playlist_of_account(self, idAccount:str):
        self.connection.open()
        sql = """
        DECLARE	@return_value int

        EXEC	@return_value = [dbo].[SPS_GetPlaylistsOfAccount]
                @idAccount = ?
        """
        self.connection.cursor.execute(sql, idAccount)
        listPlaylist = []
        rows = self.connection.cursor.fetchall()
        for row in rows:
            playlist = Playlist(row.IdPlaylist, row.Title,row.Creation,row.Cover,row.PublicPlaylist,
                row.IdPlaylistType)
            playlist.account.idAccount = row.IdAccount
            playlist.account.userName = row.UserName
            listPlaylist.append(playlist)
        self.connection.close()
        return listPlaylist



