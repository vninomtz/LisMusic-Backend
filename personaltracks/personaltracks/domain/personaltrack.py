from accounts.accounts.domain.account import Account
from uuid import uuid4
class PersonalTrack:
    def __init__(self,idPersonalTrack=None,title=None,gender=None,album=None,duration=None,fileTrack=None,available=None):
        self.idPersonalTrack = idPersonalTrack
        self.title = title
        self.gender = gender
        self.album = album
        self.duration = duration
        self.fileTrack = fileTrack
        self.available = available
        self.account:Account = Account()

    @classmethod
    def create(cls, title, gender, album, fileTrack):
        new_personal_tracks = PersonalTrack(str(uuid4()), title, gender, album, None, fileTrack, False)   
        return new_personal_tracks

    def to_json(self):
        personaltrack_to_json = {
        "idPersonalTrack": self.idPersonalTrack,
        "idAccount": self.account.idAccount,
        "title": self.title,
        "gender": self.gender,
        "album": self.album,
        "duration": self.duration,
        "fileTrack": self.fileTrack,
        "available": self.available
        
    }
        return personaltrack_to_json
