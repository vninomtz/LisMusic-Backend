

class MusicGender: 
    def __init__(self=None,idMusicGender=None,genderName=None):
        self.idMusicGender: int = idMusicGender
        self.genderName: str = genderName

    def to_json(self):
        music_gender_to_json = {
            "idMusicGender": self.idMusicGender,
            "genderName": self.genderName 
        }
        return music_gender_to_json
        