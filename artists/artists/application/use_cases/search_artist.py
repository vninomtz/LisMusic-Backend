from artists.artists.application.repositories.repository_artist import ArtistRepository
from artists.artists.domain.artist import Artist
from dataclasses import dataclass
from artists.artists.domain.exceptions import ArtistInvalidException, ArtistNotExistsException


class SearchArtist:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository

    def execute(self, queryCriterion: str):

        if not queryCriterion:
            raise ArtistInvalidException("Empty field")

        search_response = self.repository.search_artists(queryCriterion)
        if not search_response:
            raise ArtistNotExistsException("Matches not found")

        return search_response;
