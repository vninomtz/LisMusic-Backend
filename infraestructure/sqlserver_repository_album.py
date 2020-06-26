from albums.albums.domain.album import Album
from albums.albums.application.repositories.repository_album import AlbumRepository
from infraestructure.connection import ConnectionSQL
from albums.albums.domain.exceptions import DataBaseException, AlbumNotExistsException



class SqlServerAlbumRepository(AlbumRepository):
    def __init__(self):
        self.connection = ConnectionSQL()

    def save(self, album: Album):
        self.connection.open()
        sql = """
                DECLARE	@return_value int,
                @salida nvarchar(1000),
                @estado int

        EXEC	@return_value = [dbo].[SPI_CreateAlbum]
                @IdAlbum = ?,
                @Title = ?,
                @Cover = ?,
                @Publication = ?,
                @RecordCompany = ?,
                @IdMusicGender = ?,
                @IdAlbumType = ?,
                @IdArtist = ?,
                @salida = @salida OUTPUT,
                @estado = @estado OUTPUT

        SELECT	@salida as N'@salida',
                @estado as N'@estado'
        """
       
        params = (album.idAlbum,album.title,album.cover,album.publication,album.recordCompany,
                album.idMusicGender,album.idAlbumType,album.idArtist)
        print(album.idMusicGender)
        self.connection.cursor.execute(sql,params)

        try:
            self.connection.save()
            print(self.connection.cursor.rowcount, "Album created")
            self.connection.close()
            return True
        except DataBaseException as ex:
            raise DataBaseException("Database error")

    def exists_album_gender(self, idAlbumGender:str):
        self.connection.open()

        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_AlbumGenderExists]
                    @idMusicGender = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idAlbumGender)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
            
        self.connection.close()
        return result

    def exists_album_type(self, idAlbumType:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_AlbumTypeExist]
                    @idAlbumType = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idAlbumType)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
            
        self.connection.close()
        return result


