from personaltracks.personaltracks.application.repositories.repository_personal_track import PersonalTrackRepository
from personaltracks.personaltracks.domain.personaltrack import PersonalTrack
from infraestructure.connection import ConnectionSQL
from personaltracks.personaltracks.domain.exceptions import DataBaseException, TrackInvalidException


class SqlServerPersonalTrackRepository(PersonalTrackRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, personalTrack:PersonalTrack):
        self.connection.open()
        sql = """
        DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPI_CreatePersonalTrack]
                @IdPersonalTrack = ?,
                @Title = ?,
                @Duration = ?,
                @FileTrack = ?,
                @Available = ?,
                @Album = ?,
                @Gender = ?,
                @IdAccount = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """      
        params = (personalTrack.idPersonalTrack,personalTrack.title,personalTrack.duration,personalTrack.fileTrack,personalTrack.available,
        personalTrack.album,personalTrack.gender, personalTrack.account.idAccount)   

        try:
            self.connection.cursor.execute(sql,params)
            self.connection.save()
            if self.connection.cursor.rowcount > 0:
                print(self.connection.cursor.rowcount, "Personal track created")
                return True
            else:
                raise DataBaseException("Error in the personal Track creation")
        except Exception as ex:
            raise ex
        finally:
            self.connection.close()

    def update(self, personalTrack):
        self.connection.open()
        sql = """
        DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPU_UpdatePersonalTrack]
                @IdPersonalTrack = ?,
                @Title = ?,
                @Duration = ?,
                @FileTrack = ?,
                @Available = ?,
                @Album = ?,
                @Gender = ?,
                @IdAccount = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """      
        params = (personalTrack.idPersonalTrack,personalTrack.title,personalTrack.duration,personalTrack.fileTrack,personalTrack.available,
        personalTrack.album,personalTrack.gender, personalTrack.account.idAccount)
        print(params)

        try:
            self.connection.cursor.execute(sql,params)
            self.connection.save()
            if self.connection.cursor.rowcount > 0:
                print(self.connection.cursor.rowcount, "Personal track has been updated")
                return True
            else:
                raise DataBaseException("Error in the personal Track update")
        except Exception as ex:
            raise ex
        finally:
            self.connection.close()

        
        

    def get_personal_tracks_account(self, idAccount):
        self.connection.open()
        sql = """
        SELECT * FROM PersonalTracks 
        WHERE IdAccount = ?
        """
        try:  
            self.connection.cursor.execute(sql, idAccount)
            list_personaltracks = []
            rows = self.connection.cursor.fetchall()
            for row in rows:   
                personal_track = PersonalTrack(row.IdPersonalTrack,row.Title, row.Gender,
                row.Album, row.Duration,row.FileTrack, row.Available)
                personal_track.account.idAccount = row.IdAccount
                list_personaltracks.append(personal_track)
            return list_personaltracks      
        except Exception as ex:
            print(ex)
            return ex
        finally:
            self.connection.close()
        

   