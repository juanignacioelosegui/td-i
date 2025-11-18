import unittest

from ejemplos import sumar_digitos # Importamos el codigo a testear.

# Creamos una 'clase' donde incluiremos todos los tests.
class TestSumarDigitos(unittest.TestCase):
  # Definimos los casos de test, agrupando los ejemplos de
  # alguna manera significativa.
  
  def test_vacio(self):
    self.assertEqual(sumar_digitos(''), 0)

  def test_ceros(self):
    self.assertEqual(sumar_digitos('0'), 0)
    self.assertEqual(sumar_digitos('00000000000000000000'), 0)

  def test_un_digito(self):
    self.assertEqual(sumar_digitos('1'), 1)
    self.assertEqual(sumar_digitos('5'), 5)
    self.assertEqual(sumar_digitos('9'), 9)

  def test_varios(self):
    self.assertEqual(sumar_digitos('123456789'), 45)
    self.assertEqual(sumar_digitos('999'), 27)
    self.assertEqual(sumar_digitos('01230'), 6)

unittest.main()  # Una vez definidos los tests, los ejecutamos.
