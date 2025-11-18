from typing import List
##################
## EJERCICIO 1
##################

def esta_en(s: str, xs: List[str]) -> bool:
	"""Devuelve True si x está en xs
	Requiere: xs está ordenada alfabéticamente
	Devuelve:  True si y solo si hay algún 0 <= i < len(xs) tal que xs[i] == s
	Complejidad algorítmica: O(log(len(xs)))
	"""
	izq: int = 0
	der: int = len(xs)
	while izq < der:
		med: int = (izq + der) // 2
		if xs[med] == s:
			return True
		elif xs[med] < s:
			izq = med + 1
		else:
			der = med 
	return False

#################
## EJERCICIO 2 ##
#################

def distritos_donde_vota(padrones: List[List[str]], nombre: str) -> List[int]:
	"""Devuelve los índices de los distritos en donde vota alguien de nombre "nombre"
	Requiere: Para todo i, 0 <= i < len(padrones), padrones[i] está ordenado alfabéticamente
	Devuelve: Para cada elemento e de vr, vale que padrones[e] contiene el nombre "nombre"
	"""
	vr: List[int] = []
	for i in range(len(padrones)):
		padron: List[str] = padrones[i]
		if esta_en(nombre, padron):
			vr.append(i)
	return vr


padron: List[List[str]] = [
   ['Smith Alice', 'Smith Bob'],  # padrón del distrito 0
   ['Smith Carl', 'Smith Lee'],  # padrón del distrito 1
   ['Smith Alice', 'Smith Carl'],   # padrón del distrito 2
]
nombre: str = 'Smith Lee'

print(distritos_donde_vota(padron, nombre) == [1])
