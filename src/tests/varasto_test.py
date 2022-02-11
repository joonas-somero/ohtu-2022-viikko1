import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_virheellisen_tilavuuden(self):
        virheellinen_varasto = Varasto(-10)

        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0)

    def test_konstruktori_nollaa_virheellisen_alkusaldon(self):
        virheellinen_varasto = Varasto(10, -5)

        self.assertAlmostEqual(virheellinen_varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivisen_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-10)

        # varaston tulisi olla edelleen tyhjä
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tilavuuden_ylittyessa_ylimaarainen_hukataan(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 10)

        # varaston tulisi olla nyt täynnä
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivisen_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_otettaessa_yli_saldon_palautetaan_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_varasto_olio_tulostuu_oikein(self):
        self.varasto.lisaa_varastoon(8)

        merkkijono = "saldo = 8, vielä tilaa 2"

        self.assertEqual(str(self.varasto), merkkijono)
