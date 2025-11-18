from typing import List

################
# EJERCICIO 1
################
def factorial(n: int) -> int:
    '''
    Requiere: n natural
    Devuelve: la productoria entre 1 y n
    '''
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def suma_digitos(n: int) -> int:
    '''
    Requiere: n natural
    Devuelve: la suma de los digitos de n
    '''
    digito:str = str(n)
    if len(n)==1:
        return n
    else:
        return int(digito[0]) + suma_digitos(int(digito[1:]))

def suma_impares(n: int) -> int:
    '''
    Requiere: n natural
    Devuelve: la sumatoria de los primeros n-naturales impares siendo 1 el primer natural impar
    '''
    if n == 1:
        return 1
    else:
        return 2*n-1 + suma_impares(n-1)
    

################
# EJERCICIO 2a
################

### OPCIÓN 1
def sumar_n1(l:List[int], n:int) -> List[int]:
    '''
    Requiere: nada
    Devuelve: Sea L el valor de l modificada, len(L)==len(l), y en toda posición
          j entre 0 y len(l)-1:  L[j]==l[j] + n 
    '''
    if len(l) == 0: #CASO BASE
        vr:List[int] = []
        return vr
        
    else: #PASO RECURSIVO
        vr:List[int] = [l[0] + n]
        return vr + sumar_n1(l[1:] ,n)

### OPCIÓN 2
def sumar_n2(l:List[int], n:int) -> List[int]:
    '''
    Requiere: nada
    Devuelve: Sea L el valor de l modificada, len(L)==len(l), y en toda posición
          j entre 0 y len(l)-1:  L[j]==l[j] + n 
    '''
    if len(l)==0: #CASO BASE
        vr:List[int] = []
        return vr
    
    else: #PASO RECURSIVO
        vr:List[int] = sumar_n2(l[:len(l)-1], n)
        vr.append(l[len(l)-1] + n)
        return vr
    

################
# EJERCICIO 2b
################
def codificacion_inversa(xs:List[int]) -> str:
    '''
    Requiere: xs no vacia
    Devuelve: la concatenacion de los strings desde el ultimo en la lista hasta el primero.
    '''
    if len(xs)== 1:
    	return xs[0]
    else:
    	return codificacion_inversa(xs[:-1]) + xs[len(xs) - 1]
    
    
