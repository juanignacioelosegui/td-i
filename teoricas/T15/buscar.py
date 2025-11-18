from typing import List

def buscar_v1(elem:int, lista:List[int]) -> bool:
    ''' Requiere: nada
        Devuelve: True si elem está en lista; False si no.
    '''
    encontre:bool = False
    i:int = 0
    while i<len(lista):
        if lista[i]==elem:
            encontre = True
        i = i + 1
    return encontre

def buscar_v2(elem:int, lista:List[int]) -> bool:
    ''' Requiere: nada
        Devuelve: True si elem está en lista; False si no.
    '''
    encontre:bool = False
    i:int = 0
    while i<len(lista) and not encontre: 
        # En esta version, cortamos la ejecución del ciclo en  
        # cuanto encontramos al elemento buscado. Igualmente, la
        # complejidad temporal en peor caso sigue siendo lineal.
        if lista[i]==elem:
            encontre = True
        i = i + 1
    return encontre

