from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.exceptions import InvalidParamsException, DataBaseException
from tracks.tracks.domain.track import Track


class GetTracksOfPlaylist():
    def __init__(self, repository):
        self.repository:TrackRepository = repository

    def execute(self, idPlaylist:int):
        if not idPlaylist or type(idPlaylist)  != int:
            raise InvalidParamsException("Invalid params")

        try:
            listTracks:Track = self.repository.get_tracks_of_playlist(idPlaylist)
            return listTracks
        except DataBaseException as ex:
            raise DataBaseException(ex)

