from artists.artists.application.repositories.repository_artist import ArtistRepository
from artists.artists.domain.exceptions import ArtistInvalidException, DataBaseException
from dataclasses import dataclass
from artists.artists.domain.artist import Artist


@dataclass
class CreateArtistInputDto:
    name: str = None
    cover: str = None
    description: str = None
    

class CreateArtist:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository

    def execute(self, inputArtist: CreateArtistInputDto):
        if not inputArtist.name or not inputArtist.cover or not inputArtist.description:
            raise ArtistInvalidException("Empty fields.")

        new_artist = Artist.create(inputArtist.name, inputArtist.cover, inputArtist.description)

        try:
            self.repository.save(new_artist)
            return new_artist
        except DataBaseException:
            raise DataBaseException("Database error.")
