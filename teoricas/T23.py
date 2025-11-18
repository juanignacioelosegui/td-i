from typing import List

def suma(n:int) -> int:
    ''' Requiere: n>=0 
        Devuelve: la suma de los números entre 0 y n.
    '''
    if n==0:  # caso base
        return 0
    else:     # caso recursivo
        s:int = suma(n-1)
        return s + n

def maximo(xs:List[int]) -> int:
    ''' Requiere: len(xs)>0 
        Devuelve: el máximo elemento en xs.
    '''
    if len(xs) == 1:   # caso base
        return xs[0]
    else:              # caso recursivo
        m:int = maximo(xs[1:])
        if m > xs[0]:
            return m
        else:
            return xs[0]

print(suma(0))            # 0
print(suma(10))           # 55
print(maximo([123]))      # 123
print(maximo([4,1,3,7]))  # 7
