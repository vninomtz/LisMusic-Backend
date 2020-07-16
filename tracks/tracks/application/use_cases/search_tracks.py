from tracks.tracks.application.repositories.repositorie_track import TrackRepository
from tracks.tracks.domain.track import Track
from dataclasses import dataclass
from tracks.tracks.domain.exceptions import TrackInvalidException, TrackNotExistsException

class SearchTrack:
    def __init__(self, repository: TrackRepository):
        self.repository = repository

    def execute(self, queryCriterion: str):

        if not queryCriterion:
            raise TrackInvalidException("Empty field")

        search_response = self.repository.search_tracks(queryCriterion)
        if not search_response:
            raise TrackNotExistsException("Matches not found")

        return search_response;
