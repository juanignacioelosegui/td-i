import unittest

from buscar import buscar_v1, buscar_v2

class TestBuscar(unittest.TestCase):
 
  def test_buscar_v1(self):
    self.assertTrue(buscar_v1(1, [1,2,3,4,5,6]))
    self.assertTrue(buscar_v1(1, [2,3,4,1,5,6]))
    self.assertTrue(buscar_v1(1, [2,3,4,5,6,1]))
    self.assertTrue(buscar_v1(1, [2,1,3,1,4,5,6,1]))
    self.assertTrue(buscar_v1(1, [1,1,1,1]))
    self.assertTrue(buscar_v1(1, [1]))
    self.assertFalse(buscar_v1(1, [2,3,4,5,6]))
    self.assertFalse(buscar_v1(1, []))

  def test_buscar_v2(self):
    self.assertTrue(buscar_v2(1, [1,2,3,4,5,6]))
    self.assertTrue(buscar_v2(1, [2,3,4,1,5,6]))
    self.assertTrue(buscar_v2(1, [2,3,4,5,6,1]))
    self.assertTrue(buscar_v2(1, [2,1,3,1,4,5,6,1]))
    self.assertTrue(buscar_v2(1, [1,1,1,1]))
    self.assertTrue(buscar_v2(1, [1]))
    self.assertFalse(buscar_v2(1, [2,3,4,5,6]))
    self.assertFalse(buscar_v2(1, []))

unittest.main()
