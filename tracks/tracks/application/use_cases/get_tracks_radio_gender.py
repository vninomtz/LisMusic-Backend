from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.exceptions import InvalidParamsException, DataBaseException
from tracks.tracks.domain.track import Track
import random


class GetTracksRadioGender():
    def __init__(self, repository):
        self.repository:TrackRepository = repository

    def execute(self, idMusicGender:int):
        if not idMusicGender or type(idMusicGender)  != int:
            raise InvalidParamsException("Invalid params")

        try:
            listTracks:Track = self.repository.get_tracks_radio_gender(idMusicGender)
            random.shuffle(listTracks, random.random)
            return listTracks
        except DataBaseException as ex:
            raise DataBaseException(ex)