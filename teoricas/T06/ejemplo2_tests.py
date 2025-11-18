import unittest

from ejemplo2 import volumen_cilindro # Importamos el codigo a testear.

# Creamos una 'clase' donde incluiremos todos los tests.
class TestVolumenCilindro(unittest.TestCase):
  # Definimos los casos de test, agrupando los ejemplos de
  # alguna manera significativa.

  def test_valores_enteros(self):
    self.assertAlmostEqual(volumen_cilindro(1.0, 1.0), 3.14159, places=3)
    self.assertAlmostEqual(volumen_cilindro(10.0, 10.0), 3141.5927, places=3)

  def test_valores_con_parte_decimal(self):
    self.assertAlmostEqual(volumen_cilindro(12.345, 6.789), 3250.4080, places=3)
    self.assertAlmostEqual(volumen_cilindro(0.1, 0.1), 0.0031416, places=3)

#####################################################################

unittest.main()  # Una vez definido el test, lo ejecutamos.
