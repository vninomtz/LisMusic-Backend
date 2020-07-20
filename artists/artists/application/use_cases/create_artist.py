from artists.artists.application.repositories.repository_artist import ArtistRepository
from artists.artists.domain.exceptions import ArtistInvalidException, DataBaseException
from dataclasses import dataclass
from artists.artists.domain.artist import Artist
from utils.Image import Image


@dataclass
class CreateArtistInputDto:
    name: str = None
    cover: str = None
    description: str = None
    idAccount: str = None
    

class CreateArtist:
    def __init__(self, repository: ArtistRepository):
        self.repository = repository

    def execute(self, inputArtist: CreateArtistInputDto):
        if not inputArtist.name or not inputArtist.cover or not inputArtist.description or not inputArtist.idAccount:
            raise ArtistInvalidException("Empty fields.")
        
        new_artist = Artist.create(inputArtist.name, inputArtist.cover, inputArtist.description)
        new_artist.account.idAccount = inputArtist.idAccount
        nameCover = Image.generate_name(new_artist.name)
        if Image.save_image(new_artist.cover, nameCover, "Artist"):
            new_artist.cover = nameCover

        try:
            self.repository.save(new_artist)
            return new_artist
        except DataBaseException:
            raise DataBaseException("Database error.")
