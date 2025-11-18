# =============================================================================
# Ejercicio 1
# 
# Determinar a mano qué imprimen por pantalla los siguientes programas.
# =============================================================================

#a)

def f(x:str) -> str:
    return ('T' + x) * 3

r:int = f('ini')
print(r)

#b)
def g(a:int, b:int) -> float:
    return a / b 

a:int = 666
c:int = 222
r:float = g(a, c)
print(r)

#c)

def h(x:int, y:int) -> int:
    x = 10
    return x + y

b:int = 8

r:int = h(b, b)
print(r)

r = h(x, b)
print(r)

# =============================================================================
# Ejercicio 2
# 
# Dadas las siguientes funciones escritas en Python, ponerle un nombre que describa mejor lo que hace, escribir su especificación en docstring y algunos ejemplos de uso.
# =============================================================================

#a)
def f(x:int, y:int) -> float:
    return 1/x + 1/y

#b)
def g(x:int, y:int) -> float:
    a:int = x * y
    b:int = a * a
    return y/a + a*x/b

# =============================================================================
# Ejercicio 3
# 
# Para cada función:
# 
#     1) Escribir su especificación (Encabezado, Requiere y Devuelve en docstring).
#     2) Escribir ejemplos de uso (varios pares de entrada/salida).
#     3) Escribir un programa que la resuelva y asegurarse de que funcione para los ejemplos de uso.
# 
# a) Dados los puntos A y B del espacio cartesiano bidimensional, se desea calcular la distancia entre A y B. Se puede suponer que cada punto K está representado por dos enteros k1 y k2 que indican sus coordenadas en el eje X y en el eje Y respectivamente.
# 
# b) Dadas las coordenadas de los vértices opuestos de un rectángulo, se debe determinar cuál es el perímetro del rectángulo. Suponer que cada vértice está expresado mediante dos enteros, como en el punto anterior.
# =============================================================================
