import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 1010)
        
    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 990)  
        
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo, 1000)
        
    def test_palauttaa_true(self):
        result = self.maksukortti.ota_rahaa(10) 
        self.assertEqual(result, True)
        
    def test_palauttaa_false(self):
        result = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(result, False)
                
    def test_saldo_euroina(self):
        saldo = self.maksukortti.saldo_euroina()
        self.assertEqual(saldo, 10.0)
        
    def test_str(self):
        str1 = "Kortilla on rahaa 10.00 euroa"
        self.assertEqual(str(self.maksukortti), str1)
