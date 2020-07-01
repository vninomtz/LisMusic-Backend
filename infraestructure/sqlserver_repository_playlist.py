from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from infraestructure.connection import ConnectionSQL

class SqlServerPlaylistRepository(PlaylistRepository):
    def __init__(self):
        self.connection = ConnectionSQL()
    
    def save(self, playlist: Playlist):
        pass

    
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



