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

# =============================================================================
# Seguimiento del estado de las variables.
#
# Ejecuto la línea 12.
# Estado: r = f('ini') = 'TiniTiniTini'
# 
#         Ejecuto la línea 9.
#         Estado: x = 'ini'
#         
#         Ejecuto la línea 10: devuelve el valor de vr
#         Estado: x = 5, vr = ('T' + x) * 3 = 'Tini' * 3 = 'TiniTiniTini'
#     
# Ejecuto la línea 13: imprime el valor de r
# 
# FIN
# =============================================================================



#b)
def g(a:int, b:int) -> float:
    return a / b 

a:int = 666
c:int = 222
r:float = g(a, c)
print(r)

# =============================================================================
# Seguimiento del estado de las variables.
# 
# Ejecuto la línea 38.
# Estado: a = 666
# 
# Ejecuto la línea 39.
# Estado: a = 6, c = 222
# 
# Ejecuto la línea 40.
# Estado: a = 6, c = 222, r = h(a,c) = h(666, 222) = 3.0
# 
#         Ejecuto la línea 35.
#         a = 666, b = 222
# 
#         Ejecuto la línea 36: devuelve el valor de vr
#         Estado: a = 666, b = 222, vr = 666 / 222 = 3.0
# 
# Ejecuto la línea 41: imprime el valor de r
# 
# FIN
# =============================================================================

#c)


def f(x:int, y:int) -> int:
    x = 10
    return x + y

b:int = 8

r:int = f(b, b)
print(r)

r = f(x, b)
print(r)

# =============================================================================
# Seguimiento del estado de las variables.
# 
# Ejecuto la línea 73.
# Estado: b = 8
# 
# Ejecuto la línea 75.
# Estado: b = 8, r = f(b, b) = f(8, 8) = 18
# 
#         Ejecuto la línea 69.
#         Estado: x = 8, y = 8
#         
#         Ejecuto la línea 70.
#         Estado: x = 10, y = 8
#         
#         Ejecuto la línea 71: devuelve el valor de vr 
#         Estado: x = 10, y = 8, vr = x + y = 10 + 8 = 18
# 
# Ejecuto la línea 76: imprime el valor de r
# Estado: b = 8, r = 18
# 
# Ejecuto la línea 78.
# Estado: b = 8, r = f(x, b) = f(??, 8) ---> ERROR. La variable x no está definida.
# 
# FIN
# =============================================================================


# =============================================================================
# Ejercicio 2
# 
# Dadas las siguientes funciones escritas en Python, ponerle un nombre que describa mejor lo que hace, escribir su especificación en docstring y algunos ejemplos de uso.
# =============================================================================

#a)

# def f(x:int, y:int) -> float:
def sumar_inversos_multiplicativos(x:int, y:int) -> float:
    ''' Suma el inverso multiplicativo de x con el inverso multiplicativo de y.
        Requiere: x != 0, y != 0
        Devuelve: un valor flotante aprox. igual al resultado de 1/x + 1/y
    '''
    return 1/x + 1/y

# =============================================================================
# Ejemplos de uso:
#     
#     x    y    vr
#     50  50    0.04
#     2    2    1.0
#     10   1    1.1
#     1    2    1.5
#     1    1    2.0
# =============================================================================

#b)

# Se resuelve igual que el (a)
# def g(x:int, y:int) -> float:
def sumar_inversos_multiplicativos_bis(x:int, y:int) -> float:
    ''' Suma el inverso multiplicativo de x con el inverso multiplicativo de y.
        Requiere: x != 0, y != 0
        Devuelve: un valor flotante aprox. igual al resultado de 1/x + 1/y
    '''
    a:int = x * y
    b:int = a * a
    return y/a + a*x/b

# Valen los mismos ejemplos de uso.

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

# a)

import math
def distancia(x1:float, y1:float, x2:float, y2:float) -> float:
    ''' Calcula la distancia euclidiana entre los puntos (x1, y1) y (x2, y2).
        Requiere: Ninguna
        Devuelve: un valor flotante aprox. igual a raiz_cuadrada((x2-x1)^2 + (y2-y1)^2)
    '''
    dist_x:float = x2 - x1
    dist_y:float = y2 - y1
    vr:float = math.sqrt(dist_x ** 2 + dist_y ** 2)
    return vr

# Ejemplos de uso expresados con código

eps:float = 0.0000001

print(distancia(1.0, 1.0, 2.0, 1.0) - 1.0 < eps)
print(distancia(1.0, 1.0, 2.0, 2.0) - math.sqrt(2.0) < eps)
print(distancia(0.0, 0.0, 4.0, 3.0) - 5.0 < eps)

# b)

def perimetro_rectangulo(x1:float, y1:float, x2:float, y2:float) -> float:
    ''' Calcula el perímetro de un rectángulo conociendo 2 de sus vértices opuestos: (x1, y1) y (x2, y2).
        Requiere: (x1, y1) y (x2, y2) deben ser puntos distintos.
        Dvuelve: un valor flotante aprox. igual a la suma de los 4 lados del rectángulo con vértices opuestos (x1, y1) y (x2, y2)
    '''
    long_lado_1:float = abs(x1 - x2)
    long_lado_2:float = abs(y1 - y2)
    vr:float = 2 * long_lado_1 + 2 * long_lado_2
    return vr

# Ejemplos de uso expresados con código

print(perimetro_rectangulo(0.0, 0.0, 1.0, 1.0) - 4.0 < eps)
print(perimetro_rectangulo(0.0, 0.0, 2.0, 2.0) - 8.0 < eps)
print(perimetro_rectangulo(1.0, 1.0, 0.0, 0.0) - 4.0 < eps)
print(perimetro_rectangulo(1.0, 1.0, -1.0, -1.0) - 8.0 < eps)

# =============================================================================
# Comentario sobre la variable vr:
# 
# Como habrán notado, a veces definimos explícitamente la variable vr (ej. 3) y a veces no (ejs. 1 y 2).
# A la hora de programar no es estrictamente necesario definir vr y dependerá de cada problema si
# resulta conveniente o no crearla. El criterio que usamos nosotros es "si nos parece que aporta la definimos. Si no, no."
# =============================================================================
