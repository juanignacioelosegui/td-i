###########################################################
##################### Ejercicio 2 (c) #####################
###########################################################

import unittest


# Importamos el codigo a testear.
from traductor_jeringoso_bib import traducir_a_jeringoso

# Creamos una 'clase' donde incluiremos todos los tests.

class TestTraductor(unittest.TestCase):

  # Definimos los casos de test, agrupando los ejemplos de
  # alguna manera significativa.


  # Test para chequear el string vacío.
  def test_vacío(self):

    self.assertEqual(traducir_a_jeringoso(''), '')


  # Test para vocales individuales en minúscula.
  def test_una_vocal_minúscula(self):
    self.assertEqual(traducir_a_jeringoso('a'), 'apa')
    self.assertEqual(traducir_a_jeringoso('e'), 'epe')
    self.assertEqual(traducir_a_jeringoso('i'), 'ipi')
    self.assertEqual(traducir_a_jeringoso('o'), 'opo')
    self.assertEqual(traducir_a_jeringoso('u'), 'upu')

  # Test para vocales individuales en mayúscula.
  def test_una_vocal_mayúscula(self):
    self.assertEqual(traducir_a_jeringoso('A'), 'Apa')
    self.assertEqual(traducir_a_jeringoso('E'), 'Epe')
    self.assertEqual(traducir_a_jeringoso('I'), 'Ipi')
    self.assertEqual(traducir_a_jeringoso('O'), 'Opo')
    self.assertEqual(traducir_a_jeringoso('U'), 'Upu')

  # Test para textos sin vocales.
  def test_sin_vocales(self):
    self.assertEqual(traducir_a_jeringoso('bcdfghjklmnñpqrstvwxyz'), 'bcdfghjklmnñpqrstvwxyz')
    self.assertEqual(traducir_a_jeringoso('0123456789'), '0123456789')

  # Test para vocales repetidas.
  def test_vocales_repetidas(self):
    self.assertEqual(traducir_a_jeringoso('aa'), 'apaapa')
    self.assertEqual(traducir_a_jeringoso('Aa'), 'Apaapa')
    self.assertEqual(traducir_a_jeringoso('AA'), 'ApaApa')

  # Test para distintos textos.
  def test_textos(self):
    self.assertEqual(traducir_a_jeringoso('Hola, mundo.'), 'Hopolapa, mupundopo.')
    self.assertEqual(traducir_a_jeringoso('El viejo y el mar'), 'Epel vipiepejopo y epel mapar')
    self.assertEqual(traducir_a_jeringoso('Jeringoso'), 'Jeperipingoposopo')
    self.assertEqual(traducir_a_jeringoso('Torcuato Di Tella'), 'Toporcupuapatopo Dipi Tepellapa')



unittest.main()
