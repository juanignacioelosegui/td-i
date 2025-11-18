import unittest
from typing import List

from funciones import (suma_en_posiciones_impares,
                       suma_en_posiciones_impares_v2,
                       suma_en_posiciones_impares_v3,
                       suma_en_posiciones_impares_v4)


class TestSumaEnPosicionesPares(unittest.TestCase):
    def test_lista_vacia(self):
        vr: List[int] = suma_en_posiciones_impares([], 10)
        self.assertEqual(vr, [])

    def test_un_elemento(self):
        vr: List[int] = suma_en_posiciones_impares([1], 10)
        self.assertEqual(vr, [1])

    def test_suma_en_impares(self):
        l: List[int] = [1, 2, 3, 4, 5]
        vr: List[int] = suma_en_posiciones_impares(l, 10)
        self.assertEqual(vr, [1, 12, 3, 14, 5])

        vr = suma_en_posiciones_impares(l, 0)
        self.assertEqual(vr, [1, 2, 3, 4, 5])

        l = [1, 2, 3, 4, 5, 6]
        vr = suma_en_posiciones_impares(l, 1)
        self.assertEqual(vr, [1, 3, 3, 5, 5, 7])


class TestSumaEnPosicionesParesV2(unittest.TestCase):
    def test_lista_vacia(self):
        l: List[int] = []
        suma_en_posiciones_impares_v2(l, 10)
        self.assertEqual(l, [])

    def test_un_elemento(self):
        l: List[int] = [1]
        suma_en_posiciones_impares_v2(l, 10)
        self.assertEqual(l, [1])

    def test_suma_en_impares(self):
        l: List[int] = [1, 2, 3, 4, 5]
        suma_en_posiciones_impares_v2(l, 10)
        self.assertEqual(l, [1, 12, 3, 14, 5])

        l = [1, 2, 3, 4, 5]
        suma_en_posiciones_impares_v2(l, 0)
        self.assertEqual(l, [1, 2, 3, 4, 5])

        l = [1, 2, 3, 4, 5, 6]
        suma_en_posiciones_impares_v2(l, 1)
        self.assertEqual(l, [1, 3, 3, 5, 5, 7])


class TestSumaEnPosicionesParesV3(unittest.TestCase):
    def test_lista_vacia(self):
        vr: List[int] = suma_en_posiciones_impares_v3([], 10)
        self.assertEqual(vr, [])

    def test_un_elemento(self):
        vr: List[int] = suma_en_posiciones_impares_v3([1], 10)
        self.assertEqual(vr, [1])

    def test_suma_en_impares(self):
        l: List[int] = [1, 2, 3, 4, 5]
        vr: List[int] = suma_en_posiciones_impares_v3(l, 10)
        self.assertEqual(vr, [1, 12, 3, 14, 5])

        vr = suma_en_posiciones_impares_v3(l, 0)
        self.assertEqual(vr, [1, 2, 3, 4, 5])

        l = [1, 2, 3, 4, 5, 6]
        vr = suma_en_posiciones_impares_v3(l, 1)
        self.assertEqual(vr, [1, 3, 3, 5, 5, 7])


class TestSumaEnPosicionesParesV4(unittest.TestCase):
    def test_lista_vacia(self):
        l: List[int] = []
        suma_en_posiciones_impares_v4(l, 10)
        self.assertEqual(l, [])

    def test_un_elemento(self):
        l: List[int] = [1]
        suma_en_posiciones_impares_v4(l, 10)
        self.assertEqual(l, [1])

    def test_suma_en_impares(self):
        l: List[int] = [1, 2, 3, 4, 5]
        suma_en_posiciones_impares_v4(l, 10)
        self.assertEqual(l, [1, 12, 3, 14, 5])

        l = [1, 2, 3, 4, 5]
        suma_en_posiciones_impares_v4(l, 0)
        self.assertEqual(l, [1, 2, 3, 4, 5])

        l = [1, 2, 3, 4, 5, 6]
        suma_en_posiciones_impares_v4(l, 1)
        self.assertEqual(l, [1, 3, 3, 5, 5, 7])


unittest.main()
