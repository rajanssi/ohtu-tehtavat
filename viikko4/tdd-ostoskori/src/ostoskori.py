from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = [] 
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        summat = map(lambda t: t.lukumaara(), self.sisalto)
        return sum(summat)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinnat = map(lambda t: t.hinta(), self.sisalto)
        return sum(hinnat) 
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        for o in self.sisalto:
            if o.tuotteen_nimi() == ostos.tuotteen_nimi():
                o.muuta_lukumaaraa(1)
                return

        self.sisalto.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        ostos = Ostos(poistettava)
        for o in self.sisalto:
            if o.tuotteen_nimi() == ostos.tuotteen_nimi():
                if o.lukumaara() == 0:
                    self.sisalto.remove(o)
                else: 
                    o.muuta_lukumaaraa(-1)
                return

    def tyhjenna(self):
        self.sisalto.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.sisalto 
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
