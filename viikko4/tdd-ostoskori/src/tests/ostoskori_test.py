import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_sama_kuin_tuotteen_hitna(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        murot = Tuote("Murot", 5) 

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(murot)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        murot = Tuote("Murot", 5) 
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(murot)
        
        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisamisen_jalkeen_korin_hinta_on_niiden_hintojen_summa(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
 
        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
 
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        murot = Tuote("Murot", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(murot)
 
        ostos1 = self.kori.ostokset()[0]
        ostos2 = self.kori.ostokset()[1]
 
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        self.assertEqual(ostos1.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos1.lukumaara(), 1)
        self.assertEqual(ostos2.tuotteen_nimi(), "Murot")
        self.assertEqual(ostos2.lukumaara(), 1)