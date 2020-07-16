import sys
sys.path.append("")
from playlists.playlists.application.use_cases.get_playlist_of_account import GetPlaylistForAccount
from infraestructure.sqlserver_repository_playlist import SqlServerPlaylistRepository
from playlists.playlists.domain.exceptions import EmptyFieldsException
import unittest

class TestGetPlaylistForAccount(unittest.TestCase):
    
    def test_Empty_Fields(self):
        case = GetPlaylistForAccount(SqlServerPlaylistRepository())
        self.assertRaises(EmptyFieldsException, case.execute, None)

    def test_not_exists_account(self):
        case = GetPlaylistForAccount(SqlServerPlaylistRepository())
        result = case.execute("Noexits")
        self.assertEqual(result, [])

    def test_exists_account(self):
        case = GetPlaylistForAccount(SqlServerPlaylistRepository())
        result = case.execute("b485f40f-4f2b-43b6-9c6a-604875f31832")
        self.assertIsNotNone(result)



if __name__ == "__main__":
    unittest.main()