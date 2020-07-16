import sys
sys.path.append("")
import unittest
from tracks.tracks.application.use_cases.update_track import UpdateTrack, UpdateTrackInputDto
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.exceptions import TrackInvalidException, TrackNotExistsException
from tracks.tracks.domain.track import Track

class TestGetCreateAccount(unittest.TestCase):   
    def test_empty_fields(self):
        use_case = UpdateTrack(SqlServerTrackRepository())
        self.assertRaises(TrackInvalidException, use_case.execute, Track())

    def test_track_not_exists(self):
        use_case = UpdateTrack(SqlServerTrackRepository())
        self.assertRaises(TrackNotExistsException, use_case.execute, UpdateTrackInputDto('004a2196-c2ae-44e0'))


if __name__ == "__main__":
    unittest.main()