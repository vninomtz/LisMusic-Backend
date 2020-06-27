import abc 
from albums.albums.domain.album import Album

class AlbumRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, album: Album):
        pass

    @abc.abstractmethod
    def exists_album_gender(self, idAlbum: str):
        pass 

    @abc.abstractmethod
    def exists_album_type(self, idAlbum: str):
        pass

     
    @abc.abstractmethod
    def exists_album(self, idAlbum: str):
        pass  
 
    @abc.abstractmethod
    def get_albums_by_id_artist(self, idArtist: str):
        pass

"""     @abc.abstractmethod
    def update(self, album: Album):
        pass
        
    @abc.abstractmethod
    def delete(self, idAlbum: str):
        pass

  """

    

