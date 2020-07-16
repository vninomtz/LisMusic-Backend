from albums.albums.application.repositories.repository_album import AlbumRepository
from albums.albums.domain.album import Artist
from dataclasses import dataclass
from albums.albums.domain.exceptions import AlbumInvalidException, AlbumNotExistsException


class SearchAlbum:
    def __init__(self, repository: AlbumRepository):
        self.repository = repository

    def execute(self, queryCriterion: str):

        if not queryCriterion:
            raise AlbumInvalidException("Empty field")

        search_response = self.repository.search_albums(queryCriterion)
        if not search_response:
            raise AlbumNotExistsException("Matches not found")

        return search_response;
