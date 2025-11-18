from typing import List

# Completar el codigo, para construir una lista
# con los cuadrados de los primeros 100 enteros
# positivos: 1, 4, 9, 16, ..., 10000.
cuadrados:List[int] = []
i:int = 1
while i <= 100:
    cuadrados.append(i * i)
    i = i + 1

# Completar el codigo, para imprimir los elementos
# impares de la lista cuadrados.
i:int = 0
while i < len(cuadrados):
    if cuadrados[i] % 2 == 1:
        print(cuadrados[i])
    i = i + 1
