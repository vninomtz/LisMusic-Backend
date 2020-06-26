from artists.artists.domain.artist import Artist
from artists.artists.application.repositories.repository_artist import ArtistRepository
from infraestructure.connection import ConnectionSQL
from artists.artists.domain.exceptions import DataBaseException, ArtistNotExistsException
class SqlServerArtistRepository(ArtistRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, artist: Artist):
        self.connection.open()
        sql = """
                DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPI_CreateArtist]
                @IdArtist = ?,
                @Name = ?,
                @Cover = ?,
                @RegisterDate = ?,
                @Description = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT

        SELECT	@salida as N'@salida',
                @estado as N'@estado'
        """
        params = (artist.idArtist,artist.name,artist.cover,artist.registerDate,artist.description)
        self.connection.cursor.execute(sql,params)

        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, "Artist created")
            self.connection.close()
            return True
        except DataBaseException as ex:
            raise DataBaseException("Data base connection error")

    def update(self, artist: Artist):
        self.connection.open()
        sql = """
        DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPU_UpdateArtist]
                @IdArtist = ?,
                @Name = ?,
                @Cover = ?,
                @Description = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT
        """
        print(artist.description)
        params =(artist.idArtist,artist.name, artist.cover,artist.description)

        self.connection.cursor.execute(sql, params)
        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, " Artist updated")
            self.connection.close()
            return True
        except DataBaseException as ex:
            raise DataBaseException("Database connection error" + ex)


    def delete(self, artistId: str):
        self.connection.open()
        sql = """
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPD_DeleteArtist]
                    @idArtist = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT
        """
        params = (artistId)
        self.connection.cursor.execute(sql, params)
        row = self.connection.cursor.rowcount
        print(row)
        if row == -1:
            raise DataBaseException("Error deleting artist")

        try:
            self.connection.save()
            self.connection.close()
            return True
        except DataBaseException as ex:
            raise DataBaseException("Database connection error ", ex)    


    def exist_artist(self, idArtist:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_ArtistExist]
                    @IdArtist = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idArtist)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
            
        self.connection.close()
        return result
