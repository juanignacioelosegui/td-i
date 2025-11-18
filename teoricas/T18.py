from typing import List
    
def está(x:int, A:List[int]) -> bool:
    ''' Requiere: la lista A está ordenada en forma creciente.
        Devuelve: True si x está al menos una vez en la lista A;
                  False en caso contrario.
    '''
    izq:int = 0
    der:int = len(A)
    while izq < der:
        med:int = (izq+der) // 2
        if A[med] == x:
            return True
        elif A[med] < x:
            izq = med + 1
        else:
            der = med
    return False
