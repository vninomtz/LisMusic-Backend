from albums.albums.application.use_cases import exists_album, get_albums_like_of_account, get_albums_of_artist, get_albums_of_artist, search_album
from flask import Flask, request
from flask_restful import Resource
from artists.artists.domain.exceptions import ArtistNotExistsException, DataBaseException
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
from infraestructure.sqlserver_repository_album import SqlServerAlbumRepository
from artists.artists.application.use_cases import exists_artist
from albums.albums.domain.exceptions import AlbumInvalidException, AlbumNotExistsException
from accounts.accounts.domain.exceptions import AccountNotExistException
from accounts.accounts.application.use_cases import exists_account
from infraestructure.sqlserver_repository_account import SqlServerAccountRepository
from application.writer.handlers.login_handler import authorization_token
class AlbumsOfArtistHandler(Resource):
    @authorization_token
    def get(self,idArtist):    
        try:
            usecase_exists_artist = exists_artist.ExistsArtist(SqlServerArtistRepository())
            dtoclass_artist = exists_artist.ExistsArtistInputDto(idArtist)
            usecase_exists_artist.execute(dtoclass_artist)

            usecase = get_albums_of_artist.GetAlbumsOfArtist(SqlServerAlbumRepository())
            dtoclass = get_albums_of_artist.GetAlbumsOfArtistInputDto(idArtist)
            list_albums = usecase.execute(dtoclass)

            return [ob.to_json() for ob in list_albums], 200

        except ArtistNotExistsException as ex:
            return {"error": str(ex)}, 400  
        except DataBaseException as ex:
            return {"error": str(ex)}, 500
class AlbumsLikeOfAccountHandler(Resource):
    @authorization_token
    def get(self, idAccount):
        try:
            usecase_exits_account = exists_account.ExistAccount(SqlServerAccountRepository())
            usecase_exits_account.execute(idAccount)

            usecase = get_albums_like_of_account.GetAlbumsLikeOfAccount(SqlServerAlbumRepository())
            dtoclass = get_albums_like_of_account.GetAlbumsLikeOfAccountInputDto(idAccount)
            list_albums = usecase.execute(dtoclass)

            return [ob.to_json() for ob in list_albums], 200

        except AccountNotExistException as ex:
            return {"error": str(ex)}, 400
        except DataBaseException as ex:
            return {"error": str(ex)}, 500    



class SearchAlbumHandler(Resource):
    def get(self, queryCriterion):
        try:
            usecase = search_album.SearchAlbum(SqlServerAlbumRepository())
            list_albums = usecase.execute(queryCriterion)
            return [ob.to_json() for ob in list_albums], 200
        except AlbumInvalidException as ex:
            return {"error": str(ex)}, 400
        except AlbumNotExistsException as ex:
            return {"error": str(ex)}, 400
        except Exception as ex:
            return {"error": str(ex)}, 500