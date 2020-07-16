import abc 
from artists.artists.domain.artist import Artist

class ArtistRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, artist: Artist):
        pass

    @abc.abstractmethod
    def update(self, artist: Artist):
        pass
        
    @abc.abstractmethod
    def delete(self, idArtist: str):
        pass

    @abc.abstractmethod
    def exist_artist(self, idAritst: str):
        pass 

    @abc.abstractmethod
    def exist_artist(self, idArtist: str):
        pass

    @abc.abstractmethod
    def get_artists_like_of_account(self, idAccount: str):
        pass

    @abc.abstractmethod
    def search_artists(self, queryCriterion):
        pass
    

    
