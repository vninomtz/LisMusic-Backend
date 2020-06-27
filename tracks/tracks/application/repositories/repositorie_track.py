import abc 
from tracks.tracks.domain.track import Track

class TrackRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, track: Track):
        pass

    @abc.abstractmethod
    def update(self, track: Track):
        pass

    @abc.abstractmethod
    def delete(self, idTrack: str):
        pass

    @abc.abstractmethod
    def exists_track(self, idTrack: str):
        pass



