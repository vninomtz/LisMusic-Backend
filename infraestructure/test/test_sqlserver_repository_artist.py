import sys
sys.path.append("")
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
from artists.artists.domain.artist import Artist
import unittest
from artists.artists.domain.exceptions import DataBaseException

class TestSqlServerArtistRepository(unittest.TestCase):
    
    def setUp(self):
        self.repo = SqlServerArtistRepository()
        self.list_artists:Artist = self.repo.get_artists_like_of_account('7a6ea716-6725-4271-a3db-7cb032ce80dd')
    
    def test_exists_artist(self):
        result = self.repo.exist_artist('5dbe1334-2a03-47ff-9d1a-af1f4ebcddc0')
        self.assertTrue(result)

    def test_exists_artist_not_exists(self):
        result = self.repo.exist_artist('123')
        self.assertFalse(result)

    def test_save_artist(self):
        artist = Artist(idArtist="test123",name="testName", cover="testCover", registerDate='2020-07-08',description="isAtest")
        self.assertRaises(DataBaseException, self.repo.save, artist)

    def test_get_artists_like_of_account(self):
        self.assertIsInstance(self.list_artists[0], Artist)

    



if __name__ == "__main__":
    unittest.main()

