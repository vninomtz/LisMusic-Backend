import sys
sys.path.append("")
from infraestructure.sqlserver_repository_playlist import PlaylistRepository
import unittest

class TestPlaylistRepository(unittest.TestCase):
    def test_get_playlist_of_account_account_exists(self):
        repo = PlaylistRepository()
        listPlaylist = repo.get_playlist_of_account("d771a0a6-1f92-4e5e-918d-966e3c1f7b4f")
        self.assertIsNotNone(listPlaylist)
    
    def test_get_playlist_of_account_correct_account(self):
        repo = PlaylistRepository()
        listPlaylist = repo.get_playlist_of_account("d771a0a6-1f92-4e5e-918d-966e3c1f7b4f")
        self.assertEqual(listPlaylist[0].idAccount, "d771a0a6-1f92-4e5e-918d-966e3c1f7b4f")


    def test_get_playlist_of_account_accoun_not_exists(self):
        repo = PlaylistRepository()
        listPlaylist = repo.get_playlist_of_account("notexists")
        self.assertListEqual(listPlaylist,[])

if __name__ == "__main__":
    unittest.main()

