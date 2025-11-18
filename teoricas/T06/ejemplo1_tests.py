import unittest

from ejemplo1 import cant_vocales # Importamos el codigo a testear.

# Creamos una 'clase' donde incluiremos todos los tests.
class TestCantVocales(unittest.TestCase):
  # Definimos los casos de test, agrupando los ejemplos de
  # alguna manera significativa.
  
  def test_vacío(self):
    self.assertEqual(cant_vocales(''), 0)

  def test_vocales(self):
    self.assertEqual(cant_vocales('aáAÁ'), 4)
    self.assertEqual(cant_vocales('aeiouAEIOUáéíóúüÁÉÍÓÚÜ'), 22)

  def test_consonantes(self):
    self.assertEqual(cant_vocales('bcdfghjklmnñpqrstvwxyz'), 0)
    self.assertEqual(cant_vocales('BCDFGHJKLMNÑPQRSTVWXYZ'), 0)

  def test_puntuacion(self):
    self.assertEqual(cant_vocales(',.;:¿?¡!-\'" '), 0)

  def test_repetidas(self):
    self.assertEqual(cant_vocales('eeeee'), 5)

unittest.main()  # Una vez definido el test, lo ejecutamos.
