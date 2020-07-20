from artists.artists.domain.artist import Artist
from artists.artists.application.repositories.repository_artist import ArtistRepository
from infraestructure.connection import ConnectionSQL
from artists.artists.domain.exceptions import DataBaseException, ArtistNotExistsException
class SqlServerArtistRepository(ArtistRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, artist: Artist):
        try:
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
                    @IdAccount = ?,
                    @salida = @salida OUTPUT,
                    @estado = @estado OUTPUT

            SELECT	@salida as N'@salida',
                    @estado as N'@estado'
            """
            params = (artist.idArtist,artist.name,artist.cover,artist.registerDate,
                        artist.description, artist.account.idAccount)
            self.connection.cursor.execute(sql,params)
            self.connection.save()
            print(self.connection.cursor.rowcount, "Artist created")
            self.connection.close()
            return True
        except Exception as ex:
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

    def get_artists_like_of_account(self, idAccount: str):
            self.connection.open()
            sql = """\
            SET NOCOUNT ON;        
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)
            EXEC    @return_value = [dbo].[SPS_GetArtistsLikeOfAccount]
                    @idAccount = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
            """

            self.connection.cursor.execute(sql,idAccount)
            rows = self.connection.cursor.fetchall()
            list_artists = []
            for row in rows:
                artist = Artist(row.IdArtist,row.Name,row.Cover,row.RegisterDate, row.Description)
                list_artists.append(artist)

            return list_artists

    def search_artists(self, queryCriterion):
            self.connection.open()
            sql = """     
            SELECT	* FROM Artists WHERE Name Like ? + '%'
            """
            
            self.connection.cursor.execute(sql,queryCriterion)
            rows = self.connection.cursor.fetchall()
            if self.connection.cursor.rowcount != 0:
                list_artists = []
                for row in rows:
                    artist = Artist(row.IdArtist,row.Name,row.Cover,row.RegisterDate, row.Description)
                    list_artists.append(artist)
                return list_artists
            
            return False


    def get_account_artist(self, idAccount:str):
        try:
            self.connection.open()
            sql = """\
                DECLARE	@return_value int,
                        @estado int,
                        @salida nvarchar(1000)

                EXEC	@return_value = [dbo].[SPS_GetArtistOfAccount]
                        @idAccount = ?,
                        @estado = @estado OUTPUT,
                        @salida = @salida OUTPUT
                """
            self.connection.cursor.execute(sql,idAccount)
            row = self.connection.cursor.fetchone()
            if self.connection.cursor.rowcount != 0:
                artist = Artist(row.IdArtist,row.Name,row.Cover,row.RegisterDate, row.Description)
                artist.account.idAccount = row.IdAccount
                return artist
            else:
                return None
        except Exception as ex:
            raise DataBaseException("Database connection error ", ex) 
        finally:
            self.connection.close()


		
          

		