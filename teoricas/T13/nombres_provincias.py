from typing import TextIO,List

## Imprime solo los nombres de las provincias. OPCION 1
f:TextIO = open('provincias.txt')
for linea in f:
    linea = linea.rstrip()
    valores:List[str] = linea.split('___')
    print(valores[1])

print('--------------------------------------')

## Imprime solo los nombres de las provincias. OPCION 2
f:TextIO = open('provincias.txt')
for linea in f:
    linea = linea.rstrip()
    print(linea[5:])

