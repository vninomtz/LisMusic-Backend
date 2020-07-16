import sys
sys.path.append("")
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
from artists.artists.domain.artist import Artist
import unittest

class TestArtistRepository(unittest.TestCase):
    def setUp(self):
        self.repo = SqlServerArtistRepository()
        self.artist:Artist = Artist.create("Enjambre","defaultArtistCover.jpeg","Description ...")
        self.artist.account.idAccount = 'b485f40f-4f2b-43b6-9c6a-604875f31832'

    def test_create_succesful(self):
        response = self.repo.save(self.artist)
        self.assertTrue(response)



if __name__ == "__main__":
    unittest.main()
