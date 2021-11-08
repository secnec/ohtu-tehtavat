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
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_konstruktori_luo_pelaajalistan(self):
        
        self.assertAlmostEqual(len(self.statistics._players), 5)


    def test_pelaajahaku_palauttaa_oikeat_pelaajat(self):
        stub = PlayerReaderStub()
        pelaajalista = stub.get_players()
        for pelaaja in pelaajalista:
            self.assertEqual(self.statistics.search(pelaaja.name).__str__(), pelaaja.__str__())

    def test_pelaajahaku_palauttaa_None_kun_ei_tuloksia(self):

        self.assertEqual(self.statistics.search("Nykänen"), None)

    def test_joukkuehaku_palauttaa_oikeat_pelaajat(self):
        emd = [
            Player("Semenko", "EDM", 4, 12).__str__(),
            Player("Kurri",   "EDM", 37, 53).__str__(),
            Player("Gretzky", "EDM", 35, 89).__str__()
        ]
        for pelaaja in self.statistics.team("EDM"): 
            self.assertIn(pelaaja.__str__(), emd)

        self.assertEqual(self.statistics.team("PIT")[0].__str__(), Player("Lemieux", "PIT", 45, 54).__str__())

        self.assertEqual(self.statistics.team("DET")[0].__str__(), Player("Yzerman", "DET", 42, 56).__str__())

    def test_top_scorers_palauttaa_oikein(self):
        oikein = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]
        vastaus = self.statistics.top_scorers(3)
        
        for i in range(3):
            self.assertEqual(vastaus[i].__str__(), oikein[i].__str__())