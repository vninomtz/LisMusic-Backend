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
        params = (track.idTrack, track.title, track.duration, track.reproductions, track.avaible,
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
        pass

    def delete(self, idTrack: str):
        pass

    def exist_track(self, idTrack: str):
        pass

