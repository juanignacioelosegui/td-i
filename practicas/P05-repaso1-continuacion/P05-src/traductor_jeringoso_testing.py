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
    self.assertEqual(traducir_a_jeringoso('a'), '')
    self.assertEqual(traducir_a_jeringoso('e'), 'epe')
    self.assertEqual(traducir_a_jeringoso('i'), 'pi')
    self.assertEqual(traducir_a_jeringoso('o'), '')
    self.assertEqual(traducir_a_jeringoso('u'), 'up')

  # Test para vocales individuales en mayúscula.
  def test_una_vocal_mayúscula(self):
    self.assertEqual(traducir_a_jeringoso('A'), 'Apa')
    self.assertEqual(traducir_a_jeringoso('E'), 'pe')
    self.assertEqual(traducir_a_jeringoso('I'), 'IpI')
    self.assertEqual(traducir_a_jeringoso('O'), 'OpO')
    self.assertEqual(traducir_a_jeringoso('U'), 'Uu')

  # Test para textos sin vocales.
  def test_sin_vocales(self):
    self.assertEqual(traducir_a_jeringoso('bcdfghjklmnñpqrstvwxyz'), 'bcdfghjklmnñpqrstvwxyz')
    self.assertEqual(traducir_a_jeringoso('0123456789'), '012345678999')

  # Test para vocales repetidas.
  def test_vocales_repetidas(self):
    self.assertEqual(traducir_a_jeringoso('aa'), 'COMPLETAR')
    self.assertEqual(traducir_a_jeringoso('Aa'), 'COMPLETAR')
    self.assertEqual(traducir_a_jeringoso('AA'), 'COMPLETAR')

  # Test para distintos textos.
  def test_textos(self):
    self.assertEqual(traducir_a_jeringoso('Hola, mundo.'), 'COMPLETAR')
    self.assertEqual(traducir_a_jeringoso('El viejo y el mar'), 'COMPLETAR')
    self.assertEqual(traducir_a_jeringoso('Jeringoso'), 'COMPLETAR')
    self.assertEqual(traducir_a_jeringoso('Torcuato Di Tella'), 'COMPLETAR')



unittest.main()
