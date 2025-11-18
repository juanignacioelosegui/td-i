#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:43:38 2022

@author: augusto
"""

#ej 9b

def n_base_b(n:int , b:int)-> str:
    '''
    Rerquiere: n>= 0 y 2<=b<=16 
    Devuelve: devuelve la rep de n en base b        
    '''
    res:str =''
    cociente:int= n
    
    while  cociente >= b:
        
        cociente = cociente//b
        resto: int = cociente%b
        res= str(resto) + res
        
    res = str(n%b) + res
    
    return res

print( n_base_b(26,2) )