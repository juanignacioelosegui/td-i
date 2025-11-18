###########################################################
##################### Ejercicio 2 (c) #####################
###########################################################

def es_vocal(c:str) -> bool:
  '''
  Determina si un carácter corresponde a una vocal.
  Requiere: len(c) == 1.
  Devuelve: True si c es una vocal en mayúcula o minúscula y False en caso contrario.
  '''
  res:bool = (c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or
             c=='A' or c=='E' or c=='I' or c=='O' or c=='U')
  return res

def traducir_a_jeringoso(texto:str) -> str:
  '''
  Requiere: texto no contiene tildes.
  Devuelve: la traducción de texto a jeringoso.
  '''
  res:str = ''
  i:int = 0
  while i < len(texto):
    letra_actual:str = texto[i]
    res = res + letra_actual
    if es_vocal(letra_actual):
      res = res + 'p' + letra_actual.lower()
    i = i + 1
  return res

