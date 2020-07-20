from dataclasses import dataclass
from personaltracks.personaltracks.domain.personaltrack import PersonalTrack
from personaltracks.personaltracks.application.repositories.repository_personal_track import PersonalTrackRepository

@dataclass
class UpdatePersonalTrackInputDto:
    idPersonalTrack:str = None
    idAccount:str = None
    title:str = None
    gender:str = None
    album:str = None
    fileTrack:str = None
    available: bool = None
    duration: int = None

class UpdatePersonalTrack():
    def __init__(self, repository: PersonalTrackRepository):
        self.repository: PersonalTrackRepository = repository

    def execute(self, inputPersonalTrack: UpdatePersonalTrackInputDto):
        print(inputPersonalTrack.fileTrack)
        personal_track = PersonalTrack(inputPersonalTrack.idPersonalTrack,inputPersonalTrack.title, inputPersonalTrack.gender,
        inputPersonalTrack.album, inputPersonalTrack.duration,inputPersonalTrack.fileTrack, inputPersonalTrack.available)
        personal_track.account.idAccount = inputPersonalTrack.idAccount
  
        try:
            
            if self.repository.update(personal_track):
                return personal_track 
        except Exception as ex:
            raise ex
