import sys
sys.path.append("")
from infraestructure.sqlserver_repository_playlist import SqlServerPlaylistRepository
from playlists.playlists.domain.playlist import Playlist
import unittest

class TestSqlServerPlaylistRepository(unittest.TestCase):
    def setUp(self):
        self.repo = SqlServerPlaylistRepository()
        self.listPlaylist = self.repo.get_playlist_of_account("d771a0a6-1f92-4e5e-918d-966e3c1f7b4f")
        self.playlist: Playlist = Playlist(2,None, None, None,True,None)

    def test_get_playlist_of_account_account_exists(self):
        self.assertIsNotNone(self.listPlaylist)
    
    def test_get_playlist_of_account_correct_account(self):
        self.assertEqual(self.listPlaylist[0].account.idAccount, "d771a0a6-1f92-4e5e-918d-966e3c1f7b4f")


    def test_get_playlist_of_account_accoun_not_exists(self):
        listPlaylist = self.repo.get_playlist_of_account("notexists")
        self.assertListEqual(listPlaylist,[])

    def test_update_succesful(self):
        self.playlist.title = "Running"
        self.playlist.cover = "defaultPlaylistCover.jpeg"
        result = self.repo.update(self.playlist)
        self.assertTrue(result)
    
    def test_update_playlist_not_exists(self):
        self.playlist.idPlaylist = -1
        self.playlist.title = "Running"
        self.playlist.cover = "defaultPlaylistCover.jpeg"
        result = self.repo.update(self.playlist)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

