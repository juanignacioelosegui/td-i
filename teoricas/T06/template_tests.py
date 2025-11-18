import unittest

from ARCHIVO import FUNCION # Importamos el codigo a testear.

# Creamos una 'clase' donde incluiremos todos los tests.
class TestNOMBRE(unittest.TestCase):
  # Definimos los casos de test, agrupando los ejemplos de
  # alguna manera significativa.
  
  def test_XX(self):
    self.assertEqual(FUNCION(ENTRADA1), SALIDA1)
    self.assertEqual(FUNCION(ENTRADA2), SALIDA2)

  def test_YY(self):
    self.assertEqual(FUNCION(ENTRADA3), SALIDA3)
    ...

unittest.main()  # Una vez definido el test, lo ejecutamos.
