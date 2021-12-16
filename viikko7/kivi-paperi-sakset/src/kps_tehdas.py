from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPSTehdas:
    def uusi_peli(pelityyppi):
        if pelityyppi.endswith("a"):
            return KPSPelaajaVsPelaaja()
        elif pelityyppi.endswith("b"):
            return KPSTekoaly(Tekoaly())
        elif pelityyppi.endswith("c"):
            return KPSTekoaly(TekoalyParannettu(10))
        else:
            return None
