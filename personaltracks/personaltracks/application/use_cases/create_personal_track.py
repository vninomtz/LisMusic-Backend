from dataclasses import dataclass
from personaltracks.personaltracks.domain.personaltrack import PersonalTrack
from personaltracks.personaltracks.application.repositories.repository_personal_track import PersonalTrackRepository

@dataclass
class CreatePersonalTrackInputDto:
    idPersonalTrack:str = None
    idAccount:str = None
    title:str = None
    gender:str = None
    album:str = None
    fileTrack:str = None
    
class CreatePersonalTrack():
    def __init__(self, repository: PersonalTrackRepository):
        self.repository: PersonalTrackRepository = repository

    def execute(self, inputPersonalTrack: CreatePersonalTrackInputDto):
        new_personal_track = PersonalTrack.create(inputPersonalTrack.title, inputPersonalTrack.gender,inputPersonalTrack.album,inputPersonalTrack.fileTrack)
        new_personal_track.account.idAccount = inputPersonalTrack.idAccount
        try:
            if self.repository.save(new_personal_track):
                return new_personal_track
            
        except Exception as ex:
            raise ex

    
