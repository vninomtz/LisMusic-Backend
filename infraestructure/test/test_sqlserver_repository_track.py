import sys
sys.path.append("")
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.track import Track
from albums.albums.domain.album import Album
from artists.artists.domain.artist import Artist
import unittest


class TestTrackRepository(unittest.TestCase):
    def setUp(self):
        self.repo = SqlServerTrackRepository()
        self.listTracks:Track = self.repo.get_tracks_of_playlist(11)

    def test_get_tracks_of_playlist(self):
        self.assertIsNotNone(self.listTracks)

    def test_get_tracks_of_playlist_instance_track(self):
        self.assertIsInstance(self.listTracks[0], Track)
    
    def test_get_tracks_of_playlist_instance_album(self):
        self.assertIsInstance(self.listTracks[0].album, Album)
    
    def test_get_tracks_of_playlist_instance_artist(self):
        self.assertIsInstance(self.listTracks[0].album.artist, Artist)

    def test_get_tracks_radio_gender(self):
        listTracks:Track = self.repo.get_tracks_radio_gender(14)
        self.assertIsNotNone(listTracks)
    




if __name__ == "__main__":
    unittest.main()