from typing import List,Tuple

################
# EJERCICIO 1(a)
################
def potencia_de_3_a_n(n: int) -> int:
    '''
    Requiere: n natural
    Devuelve: 3^n
    '''
    if n == 1:
        return 3 #CASO BASE
    else:
        return 3 * potencia_de_3_a_n(n-1) #PASO RECURSIVO
    


################
# EJERCICIO 1(b)
################

def resto_division_por_cinco(n: int) -> int:
    '''Requiere: n natural
    Devuelve: el resto de dividir a n por 5
    '''
    if n < 5 :
        return n
    else : 
        return resto_division_por_cinco(n-5)
    
    
    
################
# EJERCICIO 1(c)
################
    
def cociente_resto_division_por_cinco(n: int) ->  Tuple[int,int]:
    '''Requiere: n natural
    Devuelve: el cociente y el resto de dividir a n por 5 en una tupla de la forma (cociente,resto)
    '''
    if n < 5 :
        return (0,n)
    else : 
        c_r :Tuple[int,int] = cociente_resto_division_por_cinco(n-5)
        return (1+c_r[0], c_r[1])
  
    
  
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
        return True 
    else :
        return xs[0] == xs[ -1] and es_capicua(xs [1: -1])



################
# EJERCICIO 3 
################
def contar_letras(xs:List[str], l:str) -> int:
    '''
    Requiere: nada
    Devuelve: la cantidad de cadenas en xs que contienen la letra l
    '''
    if len(xs) == 0:
        return tiene_letra(xs[0],l) 
    else :
        return tiene_letra(xs[0],l) + contar_letras(xs [1:],l)

def tiene_letra(s:str,l:str) -> int:
    '''
    Requiere: nada
    Devuelve: 1 si la letra l está en el string s; 0 en el caso contrario
    '''
    if l in s: return 1
    else: return 0