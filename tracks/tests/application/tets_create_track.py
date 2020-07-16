import sys
sys.path.append("")
import unittest
from tracks.tracks.application.use_cases.create_track import CreateTrack
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.exceptions import TrackInvalidException
from tracks.tracks.domain.track import Track

class TestGetCreateAccount(unittest.TestCase):   
    def test_empty_fields(self):
        use_case = CreateTrack(SqlServerTrackRepository())
        self.assertRaises(TrackInvalidException, use_case.execute, Track())


if __name__ == "__main__":
    unittest.main()