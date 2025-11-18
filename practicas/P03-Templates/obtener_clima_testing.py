import unittest
from obtener_clima import obtener_clima

class TestBotClima(unittest.TestCase):
  def test_frio(self):
    temperatura:int = 5
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'frio'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_templado(self):
    temperatura:int = 15
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'templado'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_agradable(self):
    temperatura:int = 21
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'agradable'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_caluroso(self):
    temperatura:int = 32
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'caluroso'
    self.assertEqual(respuesta_bot, respuesta_esperada)
    
  def test_menos273(self):
    temperatura:int = -273
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'frio'
    self.assertEqual(respuesta_bot, respuesta_esperada)
    
  def test_0(self):
    temperatura:int = 0
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'frio'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_10(self):
    temperatura:int = 10
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'frio'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_11(self):
    temperatura:int = 11
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'templado'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_16(self):
    temperatura:int = 16
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'templado'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_17(self):
    temperatura:int = 17
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'agradable'
    self.assertEqual(respuesta_bot, respuesta_esperada)
    
  def test_25(self):
    temperatura:int = 25
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'agradable'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_26(self):
    temperatura:int = 26
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'caluroso'
    self.assertEqual(respuesta_bot, respuesta_esperada)

  def test_126(self):
    temperatura:int = 126
    respuesta_bot:str = obtener_clima(temperatura)
    respuesta_esperada:str = 'caluroso'
    self.assertEqual(respuesta_bot, respuesta_esperada)

unittest.main()
