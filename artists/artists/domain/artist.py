from uuid import uuid4
import datetime
import hashlib

class Artist:
    def __init__(self,idArtist=None,name=None,cover=None,registerDate=None,
        description=None):
        self.idArtist = idArtist
        self.name = name
        self.cover = cover
        self.registerDate = registerDate
        self.description = description

    @classmethod
    def create(cls, name, cover, description):
        newId = str(uuid4())
        created = datetime.datetime.utcnow()
        new_artist = Artist(newId, name, cover, created, description)   
        return new_artist

    def to_json(self):
        artist_to_json = {
        "idArtist": self.idArtist,
        "name": self.name,
        "cover": self.cover,
        "registerDate": self.registerDate.strftime('%Y-%m-%d'),
        "description": self.description
    }
        return artist_to_json
