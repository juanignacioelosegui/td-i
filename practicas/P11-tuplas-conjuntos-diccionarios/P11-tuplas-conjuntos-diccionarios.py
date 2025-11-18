from typing import List, Tuple, Set, Dict

#################
## Ejercicio 1 ##
#################


def nombres_personas_mayores(personas:List[Tuple[str, int, int]], edad:int) -> Set[str]:
    #
    # Completar con su codigo aqui
    #
	return 
	

def nombres_en_comun_personas_mayores(unas_personas:List[Tuple[str, int, int]], otras_personas:List[Tuple[str, int, int]]) -> List[str]:
    #
    # Completar con su codigo aqui
    #
	return 


# Para corroborar

clorinda:List[Tuple[str, int, int]] = [("Dorotea", 14581, 82), ("Azucena", 27652, 75), ("Dorotea", 3245, 89), ("Felisberto", 987, 90)]
pirane:List[Tuple[str, int, int]] = [("Azucena", 8613, 87), ("Dorotea", 5821, 88), ("Felisberto", 2854, 89), ("Luis", 99899, 35)]             
mosconi:List[Tuple[str, int, int]] = [("Dorotea", 42939, 67), ("Luis", 1150, 90)]

print(nombres_en_comun_personas_mayores(clorinda, pirane))
print(nombres_en_comun_personas_mayores(clorinda, mosconi))
print(nombres_en_comun_personas_mayores(pirane, mosconi))
print()


#################
## Ejercicio 2 ##
#################


def dnis_mellizos(personas:List[Tuple[str, int, int]]) -> Dict[int, List[Tuple[str, int]]]:
    #
    # Completar con su codigo aqui
    #
	return 


# Para corroborar

personas:List[Tuple[str, int, int]] = [("Maria", 123456, 25), 
                                       ("Ahmed", 6841635, 81),
                                       ("Jairo", 123456, 65),
                                       ("Matias", 35512, 90),
                                       ("Tomas", 355120, 8),
                                       ("Matias", 35512, 48)]

print(dnis_mellizos(personas))
