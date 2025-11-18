import unittest
from fruta import Fruta
from carrito import Carrito

PRI:str = 'primavera'
VER:str = 'verano'
OTO:str = 'otoño'
INV:str = 'invierno'

uva:Fruta = Fruta('Uva verde', 60.0, {VER})
banana:Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
pera:Fruta = Fruta('Pera Williams', 70.0, {VER})

class TestCarrito(unittest.TestCase):
    def test_agregar(self):
        c:Carrito = Carrito()
        self.assertNotIn(uva, c.frutas_en_carrito())
        self.assertEqual(c.kilos_de_fruta(uva), 0)
        c.agregar(uva, 10)
        self.assertIn(uva, c.frutas_en_carrito())
        self.assertEqual(c.kilos_de_fruta(uva), 10)

    def test_agregar_y_sacar(self):
        c:Carrito = Carrito()
        c.agregar(uva, 10)
        self.assertEqual(c.kilos_de_fruta(uva), 10)
        c.agregar(uva, 5)
        self.assertEqual(c.kilos_de_fruta(uva), 15)
        c.sacar(uva, 12)
        self.assertEqual(c.kilos_de_fruta(uva), 3)
        c.sacar(uva, 3)
        self.assertEqual(c.kilos_de_fruta(uva), 0)
        self.assertNotIn(uva, c.frutas_en_carrito())

    def test_varias_frutas(self):
        c:Carrito = Carrito()
        c.agregar(uva, 2)
        c.agregar(banana, 3)
        c.agregar(pera, 4)
        s:float = 60.0 * 2 + 150.0 * 3 + 70.0 * 4
        self.assertAlmostEqual(c.calcular_precio_total(), s)
        self.assertEqual(c.frutas_en_carrito(), {uva, banana, pera})
        c.sacar(uva, 2)
        c.sacar(banana, 3)
        c.sacar(pera, 4)
        self.assertAlmostEqual(c.calcular_precio_total(), 0)
        self.assertEqual(c.frutas_en_carrito(), set())

unittest.main()
