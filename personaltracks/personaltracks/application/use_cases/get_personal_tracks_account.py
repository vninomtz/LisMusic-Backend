
from personaltracks.personaltracks.application.repositories.repository_personal_track import PersonalTrackRepository

class GetPersonalTracks():
    def __init__(self, repository: PersonalTrackRepository):
        self.repository: PersonalTrackRepository = repository
    
    def execute(self, idAccount):
        try:
            list_personal_tracks = self.repository.get_personal_tracks_account(idAccount)
            return list_personal_tracks 
        except Exception as ex:
            raise ex