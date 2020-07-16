from playlists.playlists.application.repository.repository_playlist import PlaylistRepository
from playlists.playlists.domain.playlist import Playlist
from dataclasses import dataclass
from playlists.playlists.domain.exceptions import PlaylistInvalidException, PlaylistNotExistException


class SearchPlaylist:
    def __init__(self, repository: PlaylistRepository):
        self.repository = repository

    def execute(self, queryCriterion: str):

        if not queryCriterion:
            raise PlaylistInvalidException("Empty field")

        search_response = self.repository.search_playlists(queryCriterion)
        if not search_response:
            raise PlaylistNotExistException("Matches not found")

        return search_response;
