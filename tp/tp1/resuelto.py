from typing import List

def filtrar_solo_CAFE(s:str) -> str:
   
    '''
    Requiere: nada
    Devuelve: Una palabra compuestas solo por las letras "C", "A", "F", "E", pudiendo estar repetidas, desordenadas y no se requieren simultaneamente. 
    '''
    s:str= s.upper()
    palabra: str = ''
    i:int = 0
    #A
    while i < len(s):
        #B
        if s[i] in 'CAFE':
            palabra = palabra + s[i]
        i = i + 1
        #C
    #D
    return palabra
 
 
def es_cafetero (numero_escrito:int) -> bool:
    '''Requiere: numero_escrito > 0
    Devuelve: True si el número hexadecimal de numero_escrito solo contiene los caracteres "C", "A", "F", "E" (sin repetir y en ese mismo orden). Caso contrario, devolverá como predeterminado False. '''

    res:bool= False
    n_hex:str= hex(numero_escrito).upper()

    if ("B" in n_hex or "D" in n_hex):
        res= False
    elif (filtrar_solo_CAFE(str(n_hex)) == 'CAFE'):
        res= True 
            
    return res
 

def n_esimo_cafetero(numero:int)->int:
    '''Requiere:  numero  >0. 
    Devuelve; La posición del n-ésimo número cafetero cuyo numero cafetero es >= 51966 (el primer numero cafetero)'''
    N_esimo:int= 51966
    num_cafes:int=1 
    #E
    while num_cafes < numero:
        #F
        N_esimo=  N_esimo+1
        if (es_cafetero(N_esimo)):
            num_cafes= num_cafes +1
        #G
    #H
    return  N_esimo 

    
def cafeteros_entre(n:int, m:int) -> List[int]:
    '''Requiere: 0<n <=m
    Devuelve: Un listado de los numeros cafeteros ubicados entre n y m (incluidos), y deben estar ordenados de menor a mayor. Es decir, [n,...,m]. 
    '''
    lista_n_m:List[int]=[]
    #W
    while n<=m:
        #X
        if (es_cafetero(n)==True):
            lista_n_m.append(n)
        n=n+1
        #Y
    #Z
    return lista_n_m