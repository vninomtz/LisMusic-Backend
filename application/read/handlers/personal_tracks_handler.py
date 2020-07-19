from flask_restful import Resource
from personaltracks.personaltracks.application.use_cases import get_personal_tracks_account
from infraestructure.sqlserver_repository_personal_track import SqlServerPersonalTrackRepository
from accounts.accounts.application.use_cases import exists_account
from infraestructure.sqlserver_repository_account import SqlServerAccountRepository
from accounts.accounts.domain.exceptions import AccountNotExistException

class PersonalTracksAccountHandler(Resource):
    def get(self, idAccount):
        try:
            use_case_existsAccount = exists_account.ExistAccount(SqlServerAccountRepository())
            use_case_existsAccount.execute(idAccount)
            use_case = get_personal_tracks_account.GetPersonalTracks(SqlServerPersonalTrackRepository())
            list_personaltracks = use_case.execute(idAccount)
            return [ob.to_json() for ob in list_personaltracks], 200 
        except AccountNotExistException as ex:
            return {"error": str(ex)}, 404
        except Exception as ex:
            print(ex)
            return {"error": str(ex)}, 500

        

