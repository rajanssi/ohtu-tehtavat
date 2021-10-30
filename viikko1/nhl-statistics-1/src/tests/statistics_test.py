import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_returns_top_scorers(self):
        top_scorers = self.statistics.top_scorers(4)
        gretzky = Player("Gretzky", "EDM", 35, 89).points
        self.assertAlmostEqual(gretzky, top_scorers[0].points)

    def test_returns_list_of_players_from_a_team(self):
        teams = self.statistics.team("EDM")
        self.assertAlmostEqual(3, teams.__len__())

    def test_returns_searched_player(self):
        player = self.statistics.search("Gretzky")
        gretzky = Player("Gretzky", "EDM", 35, 89).points
        self.assertEqual(gretzky, player.points)

    def test_returns_nothing_if_cant_find_searched_player(self):
        player = self.statistics.search("Tikkanen")
        self.assertIsNone(player)