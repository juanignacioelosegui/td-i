# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:50:04 2021

@author: vilieri.i
"""
from obtener_clima_solucion import obtener_clima

def obtener_tiempo(humedad:int) -> str:
    '''
    Requiere: 0 <= humedad <= 100
    Devuelve: 'H' si humedad > 75 y 'S' en caso contrario.
    '''
    if humedad > 75:
        vr:str = 'H'
    else:
        vr:str = 'S'
    return vr


# PROGRAMA 1
clima:str = obtener_clima(26)
humedad:str = obtener_tiempo(88)

if clima == 'frio':
  print('Hace frio.')
if clima == 'caluroso' or weather == 'hot':
  print('Hace calor.')
if humedad == 'S':
  print('El tiempo es seco.')
if humedad == 'H':
  print('El tiempo es humedo.')
  
# PROGRAMA 2
clima:str = obtener_clima(26)
humedad:str = obtener_tiempo(88)

if clima == 'frio':
  print('Hace frio.')
elif clima == 'caluroso' or weather == 'hot':
  print('Hace calor.')
elif humedad == 'S':
  print('El tiempo es seco.')
elif humedad == 'H':
  print('El tiempo es humedo.')