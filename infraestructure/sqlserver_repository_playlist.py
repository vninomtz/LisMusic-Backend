from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from infraestructure.connection import ConnectionSQL
from playlists.playlists.domain.exceptions import DataBaseException

class SqlServerPlaylistRepository(PlaylistRepository):
    def __init__(self):
        self.connection:ConnectionSQL = ConnectionSQL()
    
    def save(self, playlist: Playlist):
        self.connection.open()
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
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @salida nvarchar(1000),
                    @estado int

            EXEC	@return_value = [dbo].[SPD_DeletePlaylist]
                    @idPlaylist = ?,
                    @salida = @salida OUTPUT,
                    @estado = @estado OUTPUT
        """
        try:
            self.connection.cursor.execute(sql, playlistId)
            if self.connection.cursor.rowcount > 0:
                self.connection.save()
                return True
        except Exception as ex:
            raise DataBaseException(ex)
        finally:
            self.connection.close()

    
    def exists_playlist(self, playlistId: int):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_PlaylistExist]
                    @idPlaylist = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        try:
            self.connection.cursor.execute(sql, playlistId)
            row = self.connection.cursor.fetchval()
            if row == -1:
                return False
            else:
                return True
        except Exception as ex:
            raise DataBaseException(ex)
        finally:
            self.connection.close()
        

    
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


    def add_track(self, idPlaylist:int, idTrack:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @salida nvarchar(1000),
                    @estado int

            EXEC	@return_value = [dbo].[SPI_AddTrackToPlaylist]
                    @idPlaylist = ?,
                    @idTrack = ?,
                    @salida = @salida OUTPUT,
                    @estado = @estado OUTPUT

            SELECT	@salida as N'@salida',
                    @estado as N'@estado'
        """
        try:
            self.connection.cursor.execute(sql, idPlaylist, idTrack)
            if self.connection.cursor.rowcount > 0:
                self.connection.save()
                return True
        except Exception as ex:
            raise DataBaseException(ex)
        finally:
            self.connection.close()
        


    def remove_track(self, idPlaylist:int, idTrack:str):
        self.connection.open()
        sql = """\
           DECLARE	@return_value int,
                    @salida nvarchar(1000),
                    @estado int

            EXEC	@return_value = [dbo].[SPD_QuitTrackToPlaylist]
                    @idPlaylist = ?,
                    @idTrack = ?,
                    @salida = @salida OUTPUT,
                    @estado = @estado OUTPUT

            SELECT	@salida as N'@salida',
                    @estado as N'@estado'
        """
        try:
            self.connection.cursor.execute(sql, idPlaylist, idTrack)
            if self.connection.cursor.rowcount > 0:
                self.connection.save()
                return True
        except Exception as ex:
            raise DataBaseException(ex)
        finally:
            self.connection.close()



    def exists_track(self, idPlaylist:int, idTrack:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_TrackExistsInPlaylist]
                    @idTrack = ?,
                    @idPlaylist = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        
        try:
            self.connection.cursor.execute(sql, idTrack, idPlaylist)
            row = self.connection.cursor.fetchval()
            if row == -1:
                return False
            else:
                return True
        except Exception as ex:
            raise DataBaseException(ex)
        finally:
            self.connection.close()

    def search_playlists(self, queryCriterion):
            self.connection.open()
            sql = """\

            EXEC   [dbo].[SPS_SearchPlaylists]
            @queryCriterion = ?
            """
            self.connection.cursor.execute(sql,queryCriterion)
            rows = self.connection.cursor.fetchall()
            if self.connection.cursor.rowcount != 0:
                list_playlists = []
                for row in rows:
                    playlist = Playlist(row.IdPlaylist, row.Title,row.Creation,row.Cover,row.PublicPlaylist,
                    row.IdPlaylistType)
                    playlist.account.idAccount = row.IdAccount
                    playlist.account.userName = row.UserName
                    list_playlists.append(playlist)
                return list_playlists
            
            return False
