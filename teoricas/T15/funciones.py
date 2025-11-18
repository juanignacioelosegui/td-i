from typing import List

def sumatoria(n:int) -> int:
    ''' Requiere: n>0.
        Devuelve: la suma de los enteros entre 1 y n (inclusive).
    '''
    vr:int = 0
    i:int = 1
    while i <= n:
        vr = vr + i
        i = i + 1
    return vr

def lista_sumatorias_v1(n:int) -> List[int]:
    ''' Requiere: n>=0.
        Devuelve: una lista de longitud n, que en cada posición i tenga
                  la sumatoria entre 1 e i+1.
    '''
    vr:List[int] = []
    i:int = 1
    while i<=n:
        vr.append(sumatoria(i))
        i = i + 1
    return vr

def lista_sumatorias_v2(n:int) -> List[int]:
    ''' Requiere: n>=0.
        Devuelve: una lista de longitud n, que en cada posición i tenga
                  la sumatoria entre 1 e i+1.
    '''
    vr:List[int] = []
    i:int = 1
    s:int = 1
    while i<=n:
        vr.append(s)
        i = i + 1
        s = s + i
    return vr
