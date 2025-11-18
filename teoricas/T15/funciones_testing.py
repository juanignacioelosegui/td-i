import unittest
from funciones import sumatoria, lista_sumatorias_v1, lista_sumatorias_v2

class TestSumatoria(unittest.TestCase):
 
  def test_sumatoria(self):
    self.assertEqual(sumatoria(1), 1)
    self.assertEqual(sumatoria(2), 3)
    self.assertEqual(sumatoria(3), 6)
    self.assertEqual(sumatoria(4), 10)
    self.assertEqual(sumatoria(5), 15)
    self.assertEqual(sumatoria(678), 678*679//2)
    self.assertEqual(sumatoria(999), 999*1000//2)

class TestListaSumatorias(unittest.TestCase):
 
  def test_vacia(self):
    self.assertEqual(lista_sumatorias_v1(0), [])
    self.assertEqual(lista_sumatorias_v2(0), [])

  def test_uno(self):
    self.assertEqual(lista_sumatorias_v1(1), [1])
    self.assertEqual(lista_sumatorias_v2(1), [1])

  def test_cinco(self):
    self.assertEqual(lista_sumatorias_v1(5), [1,3,6,10,15])
    self.assertEqual(lista_sumatorias_v2(5), [1,3,6,10,15])

  def test_diez(self):
    self.assertEqual(lista_sumatorias_v1(10), [1,3,6,10,15,21,28,36,45,55])
    self.assertEqual(lista_sumatorias_v2(10), [1,3,6,10,15,21,28,36,45,55])

unittest.main()
