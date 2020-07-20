
from artists.artists.application.repositories.repository_artist import ArtistRepository
from artists.artists.domain.exceptions import DataBaseException
from dataclasses import dataclass
import json

class GetArtistsAccount:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository
       
    def execute(self, idAccount:str):
        try:
            account = self.repository.get_account_artist(idAccount)
            return account
        except DataBaseException as ex:
            raise DataBaseException(ex)