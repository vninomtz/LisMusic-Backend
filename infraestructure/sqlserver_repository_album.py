from albums.albums.domain.album import Album
from albums.albums.application.repositories.repository_album import AlbumRepository
from infraestructure.connection import ConnectionSQL
from albums.albums.domain.exceptions import DataBaseException, AlbumNotExistsException

from flask import jsonify
import json
from tracks.tracks.domain.track import Track

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
                album.idMusicGender,album.idAlbumType,album.artist.idArtist)
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

    def exists_album(self, idAlbum:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_AlbumExists]
                    @IdAlbum = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idAlbum)
        row = self.connection.cursor.fetchval()
        result = False
        if row == -1:
            result = False
        else:
            result = True
            
        self.connection.close()
        return result

    def get_albums_of_artist(self, idArtist:str):
        self.connection.open()
        sql = """\
            DECLARE	@return_value int,
                    @estado int,
                    @salida nvarchar(1000)

            EXEC	@return_value = [dbo].[SPS_GetAlbumsOfArtist]
                    @IdArtist = ?,
                    @estado = @estado OUTPUT,
                    @salida = @salida OUTPUT

            SELECT	@estado as N'@estado',
                    @salida as N'@salida'
        """
        self.connection.cursor.execute(sql, idArtist)
        rows = self.connection.cursor.fetchall()
        list_albums = []
        for row in rows:
            album = Album(row.IdAlbum,row.Title,row.AlbumCover,row.Publication, row.RecordCompany,row.IdAlbumType)
            album.artist.idArtist = row.IdArtist
            album.artist.name = row.ArtistName
            album.artist.registerDate = row.RegisterDate
            album.artist.description = row.Description
            album.artist.cover = row.ArtistCover
            album.musicGender.idMusicGender = row.IdMusicGender
            album.musicGender.genderName = row.GenderName

            list_albums.append(album)

        return list_albums

    def get_albums_like_of_account(self, idAccount: str):
        sql = """\
        SET NOCOUNT ON;    
        DECLARE	@return_value int,
                @estado int,
                @salida nvarchar(1000)
         EXEC    @return_value = [dbo].[SPS_GetAlbumsLikeOfAccount]
                @idAccount = ?,
                @estado = @estado OUTPUT,
                @salida = @salida OUTPUT

        SELECT	@estado as N'@estado',
                @salida as N'@salida'
        """
        try:
            self.connection.open()
            self.connection.cursor.execute(sql,idAccount)
            pass
        except DataBaseException as ex:
            raise ("Database connection error")
        rows = self.connection.cursor.fetchall()
        list_albums = []
        for row in rows:
            album = Album(row.IdAlbum,row.Title,row.Cover,row.Publication, row.RecordCompany,row.IdAlbumType)
            album.musicGender.idMusicGender = row.IdMusicGender
            album.musicGender.genderName = row.GenderName
            album.artist.name = row.ArtistName
            album.artist.cover = row.ArtistCover
            album.artist.description = row.Description
            album.artist.registerDate = row.RegisterDate
            album.artist.idArtist = row.IdArtist
            list_albums.append(album)

        return list_albums
            
    def update(self, album: Album):
        pass
        

    def delete(self, idAlbum: str):
        pass

    def search_albums(self, queryCriterion):
        self.connection.open()
        sql = """\

         EXEC   [dbo].[SPS_SearchAlbums]
                @queryCriterion = ?
        """
        self.connection.cursor.execute(sql,queryCriterion)
        rows = self.connection.cursor.fetchall()
        if self.connection.cursor.rowcount != 0:
            list_albums = []
            for row in rows:
                album = Album(row.IdAlbum,row.Title,row.AlbumCover,row.Publication, row.RecordCompany,row.IdAlbumType)
                album.musicGender.idMusicGender = row.IdMusicGender
                album.musicGender.genderName = row.GenderName
                album.artist.name = row.ArtistName
                album.artist.cover = row.ArtistCover
                album.artist.description = row.Description
                album.artist.registerDate = row.RegisterDate
                album.artist.idArtist = row.IdArtist
                list_albums.append(album)
            return list_albums
            
        return False