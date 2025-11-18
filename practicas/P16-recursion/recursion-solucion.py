from typing import List

################
# EJERCICIO 1(a)
################
def potencia_de_3_a_n(n: int) -> int:
    '''
    Requiere: n >= 0
    Devuelve: 3^n
    '''
    if n == 0:
        return 1 #CASO BASE
    else:
        return 3 * potencia_de_3_a_n(n-1) #PASO RECURSIVO
    


################
# EJERCICIO 1(b)
################

def resto_division_por_cinco(n: int) -> int:
    '''Requiere: n >= 0
    Devuelve: el resto de dividir a n por 5
    '''
    if n < 5 :
        return n #CASO BASE
    else: 
        return resto_division_por_cinco(n-5) #PASO RECURSIVO
        
    
 
################
# EJERCICIO 2
################

def es_capicua(xs:List[int]) -> bool:
    '''
    Requiere: nada
    Devuelve: True si xs es una lista de números capicua (es la misma si se lee tanto al derecho como al revés);
              False en caso contrario
    '''
    if len (xs) == 0:
        return True #CASO BASE
    else:
        return xs[0] == xs[ -1] and es_capicua(xs [1: -1]) #PASO RECURSIVO



################
# EJERCICIO 3 
################
def contar_letras(xs:List[str], l:str) -> int:
    '''
    Requiere: nada
    Devuelve: la cantidad de cadenas en xs que contienen a la letra l
    '''
    if len(xs) == 0:
        return 0 #CASO BASE
    else:
        return uno_si_tiene_letra(xs[0],l) + contar_letras(xs [1:],l) #PASO RECURSIVO

def uno_si_tiene_letra(s:str,l:str) -> int:
    '''
    Requiere: nada
    Devuelve: 1 si la letra l está en el string s; 0 en el caso contrario
    '''
    if l in s: 
        return 1
    else: 
        return 0