import sys
sys.path.append("")
import unittest
from tracks.tracks.application.use_cases.get_track import GetTrack
from infraestructure.sqlserver_repository_track import SqlServerTrackRepository
from tracks.tracks.domain.exceptions import TrackInvalidException, TrackNotExistsException
from tracks.tracks.domain.track import Track
from tracks.tracks.application.use_cases.exists_track import ExistsTrackInputDto

class TestGetTrack(unittest.TestCase):   
    def test_empty_fields(self):
        use_case = GetTrack(SqlServerTrackRepository())
        self.assertRaises(TrackInvalidException, use_case.execute, None)

    def test_track_not_exists(self):
        use_case = GetTrack(SqlServerTrackRepository())
        self.assertRaises(TrackNotExistsException, use_case.execute, ExistsTrackInputDto('004a2196-c2ae-44e0'))    




if __name__ == "__main__":
    unittest.main()