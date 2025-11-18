import unittest
from fruta import Fruta
from catalogo import Catalogo
from typing import List

PRI:str = 'primavera'
VER:str = 'verano'
OTO:str = 'otoño'
INV:str = 'invierno'

class TestCarrito(unittest.TestCase):
    def test_csv_vacio(self):
        # El archivo frutas-para-testing1.csv está vacío.
        cat:Catalogo = Catalogo('frutas-para-testing1.csv')
        self.assertEqual(cat.frutas_de_estacion(PRI), [])
        self.assertEqual(cat.frutas_de_estacion(VER), [])
        self.assertEqual(cat.frutas_de_estacion(OTO), [])
        self.assertEqual(cat.frutas_de_estacion(INV), [])

    def test_csv_no_vacio(self):
        # El archivo frutas-para-testing2.csv tiene estas frutas:
        # Banana de Ecuador,150,"primavera,otoño,invierno"
        # Uva verde,60,verano
        # Frutillas,197.5,"primavera,verano"
        cat:Catalogo = Catalogo('frutas-para-testing2.csv')

        fru_pri:List[Fruta] = cat.frutas_de_estacion(PRI)
        self.assertEqual(len(fru_pri), 2)

        self.assertEqual(len(cat.frutas_de_estacion(VER)), 2)
        self.assertEqual(len(cat.frutas_de_estacion(OTO)), 1)

        fru_inv:List[Fruta] = cat.frutas_de_estacion(INV)
        self.assertEqual(len(fru_inv), 1)

    def test_frutas_de_primavera(self):
        cat:Catalogo = Catalogo('frutas-para-testing2.csv')
        fs:List[Fruta] = cat.frutas_de_estacion(PRI)
        self.assertEqual(len(fs), 2)
        fs.sort()
        self.assertEqual(fs[0].nombre, 'Banana de Ecuador')
        self.assertEqual(fs[1].nombre, 'Frutillas')
        
    def test_frutas_de_invierno(self):
        cat:Catalogo = Catalogo('frutas-para-testing2.csv')
        fs:List[Fruta] = cat.frutas_de_estacion(INV)
        self.assertEqual(len(fs), 1)
        self.assertEqual(fs[0].nombre, 'Banana de Ecuador')

unittest.main()
