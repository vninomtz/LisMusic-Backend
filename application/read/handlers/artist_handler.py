from artists.artists.application.use_cases import get_artists_like_of_account
from infraestructure.sqlserver_repository_account import SqlServerAccountRepository
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
from accounts.accounts.domain.exceptions import AccountNotExistException, DataBaseException
from flask_restful import Resource
from accounts.accounts.application.use_cases import exists_account

class ArtistsLikeOfAccountHandler(Resource):
    def get(self, idAccount):
        try:
            usecase_exits_account = exists_account.ExistAccount(SqlServerAccountRepository())
            usecase_exits_account.execute(idAccount)

            usecase = get_artists_like_of_account.GetArtistsLikeOfAccount(SqlServerArtistRepository())
            dtoclass = get_artists_like_of_account.GetArtistsLikeOfAccountInputDto(idAccount)
            list_artists = usecase.execute(dtoclass)

            return [ob.to_json() for ob in list_artists], 200

        except AccountNotExistException as ex:
            return {"error": str(ex)}, 400
        except DataBaseException as ex:
            return {"error": str(ex)}, 500    