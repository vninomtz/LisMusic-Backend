from flask_restful import Resource, request 
from personaltracks.personaltracks.application.use_cases import create_personal_track, update_personal_track
from infraestructure.sqlserver_repository_personal_track import SqlServerPersonalTrackRepository

class PersonalTrackHandler(Resource):
    def post(self):
        use_case = create_personal_track.CreatePersonalTrack(SqlServerPersonalTrackRepository())
        dtoclass = create_personal_track.CreatePersonalTrackInputDto(
            None,
            request.json["idAccount"],
            request.json["title"],
            request.json["gender"],
            request.json["album"],
            request.json["fileTrack"],          
        )
        try:
            personal_track = use_case.execute(dtoclass)
            return personal_track.to_json(), 200
        except Exception as ex:
            return {"error": str(ex)}, 500

    def put(self):
        use_case = update_personal_track.UpdatePersonalTrack(SqlServerPersonalTrackRepository())
        dtoclass = update_personal_track.UpdatePersonalTrackInputDto(
            request.json["idPersonalTrack"],
            request.json["idAccount"],
            request.json["title"],
            request.json["gender"],
            request.json["album"],
            request.json["fileTrack"],  
            request.json["available"], 
            request.json["duration"]       
        )
        try:
            personal_track = use_case.execute(dtoclass)
            return {}, 200
        except Exception as ex:
            return {"error": str(ex)}, 500
    
    
