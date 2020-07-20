from personaltracks.personaltracks.domain.personaltrack import PersonalTrack
import abc 

class PersonalTrackRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, personalTrack: PersonalTrack):
        pass

    @abc.abstractmethod
    def update(self, personalTrack: PersonalTrack):
        pass
    
    @abc.abstractmethod
    def get_personal_tracks_account(self, idAccount:str):
        pass