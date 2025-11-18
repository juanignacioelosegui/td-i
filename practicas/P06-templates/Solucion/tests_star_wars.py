import unittest

from star_wars import nave_estelar_cercana


class TestMision(unittest.TestCase):
    
	def test_verdaderos(self):

		self.assertTrue(nave_estelar_cercana([200,300,100], 150))
		self.assertTrue(nave_estelar_cercana([200,300,100], 100))
		self.assertTrue(nave_estelar_cercana([100,300,200], 100))
		self.assertTrue(nave_estelar_cercana([300,99,200], 100))		

	def test_falsos(self):

		self.assertFalse(nave_estelar_cercana([], 50))
		self.assertFalse(nave_estelar_cercana([], 0))		
		self.assertFalse(nave_estelar_cercana([51,300,100], 50))
		self.assertFalse(nave_estelar_cercana([200,300,100], 50))
                 
        
unittest.main()

