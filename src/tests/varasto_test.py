import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

        saatu_maara2 = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara2, 0)

        saatu_maara3 = self.varasto.ota_varastosta(50)
        self.assertAlmostEqual(saatu_maara3, 6)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisataan_likka(self):
        self.varasto.lisaa_varastoon(1000)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisataan_negatiivinen(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, saldo_ennen)

    def test_negatiivinen_varasto_luonti(self):
        uusi_varasto = Varasto(-10, -10)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)

    def test_alkusaldo_enemmankuin_tilavuus(self):
        uusi_varasto = Varasto(10, 15)
        
        self.assertAlmostEqual(uusi_varasto.saldo, 10)


    def test_teksti(self):
        tulostus = str(self.varasto)

        self.assertEqual(tulostus, "saldo = 0, vielä tilaa 10")