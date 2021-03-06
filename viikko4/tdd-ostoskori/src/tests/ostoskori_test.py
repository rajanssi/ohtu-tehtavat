import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    # 3 
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)
    
    # 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        murot = Tuote("Murot", 5) 

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(murot)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    # 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        murot = Tuote("Murot", 5) 
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(murot)
        
        self.assertEqual(self.kori.hinta(), 8)
    
    # 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # 7
    def test_kahden_saman_tuotteen_lisamisen_jalkeen_korin_hinta_on_niiden_hintojen_summa(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.assertEqual(self.kori.hinta(), 6)

    # 8 
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
 
        # testaa ett?? metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)
    
    # 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
 
        # testaa t????ll??, ett?? palautetun listan ensimm??inen ostos on halutunkaltainen.
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    # 10 
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        murot = Tuote("Murot", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(murot)
 
        ostos1 = self.kori.ostokset()[0]
        ostos2 = self.kori.ostokset()[1]
 
        # testaa t????ll??, ett?? palautetun listan ensimm??inen ostos on halutunkaltainen.
        self.assertEqual(ostos1.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos1.lukumaara(), 1)
        self.assertEqual(ostos2.tuotteen_nimi(), "Murot")
        self.assertEqual(ostos2.lukumaara(), 1)
    
    # 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_yhden_ostoksen(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_ostoksen_jonka_lukumaara_on_kaksi(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.lukumaara(), 2)

    # 13
    def test_jos_korissa_on_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jaa_koriin_yksi_tuote(self):
        maito1 = Tuote("Maito", 3)
        maito2 = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito1)
        self.kori.lisaa_tuote(maito2)

        self.kori.poista_tuote(maito1)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # 14
    def test_jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_kori_on_tyhja(self):
        maito1 = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito1)
        self.kori.poista_tuote(maito1)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    # 15
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito1 = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito1)
        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
