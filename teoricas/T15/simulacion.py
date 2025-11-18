from typing import List
from funciones import sumatoria, lista_sumatorias_v1, lista_sumatorias_v2
import time

########################

n:int = 0
ns:List[int] = []
ts:List[float] = []
res:List[int] = []
while n<=1000:
    comienzo:float = time.time()     # Tomo nota del tiempo de comienzo.
    res = lista_sumatorias_v1(n)     # Cambiar v1/v2.
    t:float = time.time() - comienzo # Calculo el tiempo usado.
    ns.append(n)
    ts.append(t)
    n = n + 10

########################

# Para usar esto, primero puede ser necesario instalar matplotlib.
# Consultar https://matplotlib.org/stable/users/installing.html
import matplotlib.pyplot as plt
plt.plot(ns, ts)
plt.xlabel('n')
plt.ylabel('tiempo')
plt.show()
