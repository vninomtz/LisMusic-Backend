from infraestructure.connection import ConnectionSQL
from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.track import Track
from tracks.tracks.domain.exceptions import DataBaseException

class SqlServerTrackRepository(TrackRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, track: Track):
        self.connection.open()
        sql = """
        DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPI_CreateTrack]
                @IdTrack = ?,
                @Title = ?,
                @Duration = ?,
                @Reproduction = ?,
                @FileTrack = ?,
                @avaible = ?,
                @IdAlbum = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """
        params = (track.idTrack, track.title, track.duration, track.reproductions, track.fileTrack, track.avaible,
                    track.album.idAlbum)
        self.connection.cursor.execute(sql,params)
        try:
            self.connection.save()
            if self.connection.cursor.rowcount > 0:
                print(self.connection.cursor.rowcount, "Track created")
                return True
            else:
                raise DataBaseException("Error in the Track creation")
        except Exception as ex:
            print(ex)
            raise DataBaseException("Data base connection error")
        finally:
            self.connection.close()

    def update(self, track: Track):
        self.connection.open()
        sql = """
        DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPU_UpdateTrack]
                @idTrack = ?,
                @title = ?,
                @duration = ?,
                @reproductions = ?,
                @fileTrack = ?,
                @avaible = ?,
                @idAlbum = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """        
        params = (track.idTrack, track.title, track.duration, track.reproductions, track.fileTrack, track.avaible,
                    track.album.idAlbum)
        print(params)            
        try:
            self.connection.cursor.execute(sql, params)

            self.connection.save()
            print(self.connection.cursor.rowcount, " Track updated")
            self.connection.close()
        
            return True
        except Exception as ex:
            
            raise ex        

    def delete(self, idTrack: str):
        pass

    def exists_track(self, idTrack: str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_TrackExists]
                    @IdTrack = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idTrack)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
            
        self.connection.close()
        return result  

    def get_tracks_of_playlist(self, idPlaylist:int):
        self.connection.open()
        sql = """
            DECLARE	@return_value int

            EXEC	@return_value = [dbo].[SPS_GetTracksOfPlaylist]
                    @idTrack = ?
        """
        self.connection.cursor.execute(sql, idPlaylist)
        rows = self.connection.cursor.fetchall()
        listTracks = []
        for row in rows:
            track = Track(row.IdTrack,row.TitleTrack,row.Duration,None,row.FileTrack,row.Avaible)
            track.album.idAlbum = row.IdAlbum
            track.album.title = row.TitleAlbum
            track.album.cover = row.CoverAlbum
            track.album.publication = row.Publication
            track.album.recordCompany = row.RecordCompany
            track.album.idAlbumType = row.IdAlbumType
            track.album.artist.idArtist = row.IdArtist
            track.album.artist.name = row.Name
            track.album.artist.cover = row.CoverArtist
            track.album.artist.registerDate = row.RegisterDate
            track.album.artist.description = row.Description
            track.album.musicGender.idMusicGender = row.IdMusicGender
            track.album.musicGender.genderName = row.GenderName
            listTracks.append(track)

        self.connection.close()
        return listTracks

    
    def get_track(self, idTrack:str):
        self.connection.open()
        sql = "Select * FROM Tracks WHERE IdTrack = ?"
        try:
            self.connection.cursor.execute(sql, idTrack)
            row = self.connection.cursor.fetchone()
            return Track(row.IdTrack,row.Title,row.Duration,row.Reproductions, row.FileTrack, row.Avaible)
        except Exception as ex:
            raise DataBaseException("Data base connection error")
        finally:
            self.connection.close()

    def search_tracks(self, queryCriterion:str):
            self.connection.open()
            sql = """\

            EXEC   [dbo].[SPS_SearchTracks]
                    @queryCriterion = ?
            """
            self.connection.cursor.execute(sql, queryCriterion)
            rows = self.connection.cursor.fetchall()
            listTracks = []
            if self.connection.cursor.rowcount != 0:
                for row in rows:
                  
                    track = Track(row.IdTrack,row.Title,row.Duration,row.Reproductions,row.FileTrack,row.Avaible)
                    track.album.idAlbum = row.IdAlbum
                    track.album.title = row.AlbumTitle
                    track.album.cover = row.Cover
                    track.album.publication = row.Publication
                    track.album.recordCompany = row.RecordCompany
                    track.album.idAlbumType = row.IdAlbumType
                    track.album.artist.idArtist = row.IdArtist
                    track.album.artist.name = row.ArtistName 
                    track.album.artist.registerDate = row.RegisterDate
                    track.album.artist.description = row.Description
                    track.album.musicGender.idMusicGender = row.IdMusicGender
                    track.album.musicGender.genderName = row.GenderName
                    
                    listTracks.append(track)
                return listTracks        
            return False


    def get_tracks_radio_gender(self, idMusicGender:int):
        try:
            self.connection.open()
            sql = """\
                DECLARE	@return_value int

                EXEC	@return_value = [dbo].[SPS_GetRadioByGender]
                        @IdMusicGender = ?
                """
            self.connection.cursor.execute(sql, idMusicGender)
            rows = self.connection.cursor.fetchall()
            listTracks = []
            if self.connection.cursor.rowcount != 0:
                for row in rows:
                    track = Track(row.IdTrack,row.TrackTitle,row.Duration,row.Reproductions,row.FileTrack,row.Avaible)
                    track.album.idAlbum = row.IdAlbum
                    track.album.title = row.AlbumTitle
                    track.album.cover = row.AlbumCover
                    track.album.publication = row.Publication
                    track.album.recordCompany = row.RecordCompany
                    track.album.artist.idArtist = row.IdArtist
                    track.album.artist.name = row.ArtistName
                    track.album.artist.cover = row.ArtistCover
                    track.album.artist.description = row.Description
                    listTracks.append(track)
                

            return listTracks
        except Exception as ex:
            raise DataBaseException("Database connection error")
        finally:
            self.connection.close()

   
    def add_track_played(self, idTrack, reproductionDate, idAccount):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPI_AddTrackToHistory]
                    @reproductionDate = ?,
                    @idAccount = ?,
                    @idTrack = ?,                    
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
            """

        try:
            params = (reproductionDate,idAccount,idTrack)
            print(params)
            self.connection.cursor.execute(sql, params)
            self.connection.save()
            self.connection.close()
            return True
        except Exception as ex:
            raise ex

    def get_tracks_account_history(self, idAccount):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_GetTracksHistoryAccount]
                    @idAccount = ?,                  
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
            """

        try:
            self.connection.cursor.execute(sql, idAccount)
            rows = self.connection.cursor.fetchall()
            list_tracks = []

            if self.connection.cursor.rowcount != 0:
                for row in rows:
                    print(row)
                    track = Track(row.IdTrack,row.Title,row.Duration,row.Reproductions,row.FileTrack,row.Avaible)
                    track.album.title = row.AlbumTitle
                    track.album.cover = row.Cover
                    track.album.artist.name = row.ArtistName 
                    track.musicGender.idMusicGender = row.IdMusicGender
                    track.musicGender.genderName = row.GenderName
                    list_tracks.append(track)
                return list_tracks      

        except Exception as ex:
            print(ex)
            raise DataBaseException("Database connection error")
        finally:
            self.connection.close();