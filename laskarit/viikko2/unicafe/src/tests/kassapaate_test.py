import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        
    def test_oikea_maara_rahaa_ja_lounaita(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kateisosto_edullinen_maksu_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kateisosto_edullinen_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_kateisosto_maukas_maksu_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukas_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_edullinen_tarpeeksi_rahaa(self):
        kassapaate = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(kassapaate)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_korttiosto_edullinen_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(800)
        kassapaate = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(kassapaate)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_korttiosto_maukas_tarpeeksi_rahaa(self):
        kassapaate = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(kassapaate)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_korttiosto_maukas_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(800)  
        kassapaate = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(kassapaate)
        self.assertEqual(self.maksukortti.saldo, 200) 
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_korttiosto_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 
        
    def test_kortin_lataus(self):    
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 600)
        self.assertEqual(self.maksukortti.saldo, 1600) 
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100600)
        
    def test_kortin_lataus_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -600)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_rahaa_euroina(self):
        eurot = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(eurot, 1000.0)
