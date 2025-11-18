import unittest
from fruta import Fruta

PRI:str = 'primavera'
VER:str = 'verano'
OTO:str = 'otoño'
INV:str = 'invierno'

class TestFruta(unittest.TestCase):
    def test_disponible_en(self):
        f1:Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
        self.assertTrue(f1.disponible_en(PRI))
        self.assertFalse(f1.disponible_en(VER))
        self.assertTrue(f1.disponible_en(OTO))
        self.assertTrue(f1.disponible_en(INV))

        f2:Fruta = Fruta('Pera Williams', 70.0, {VER})
        self.assertFalse(f2.disponible_en(PRI))
        self.assertTrue(f2.disponible_en(VER))
        self.assertFalse(f2.disponible_en(OTO))
        self.assertFalse(f2.disponible_en(INV))

    def test_menor(self):
        f1:Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
        f2:Fruta = Fruta('Pera Williams', 70.0, {VER})
        self.assertTrue(f2 < f1)
        self.assertFalse(f1 < f2)
        self.assertFalse(f1 < f1)
        self.assertFalse(f2 < f2)

    def test_repr(self):
        f1:Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
        f2:Fruta = Fruta('Pera Williams', 70.0, {VER})
        self.assertEqual(str(f1), 'Banana de Ecuador ($150.0/kg)')        
        self.assertEqual(str(f2), 'Pera Williams ($70.0/kg)')        

unittest.main()
