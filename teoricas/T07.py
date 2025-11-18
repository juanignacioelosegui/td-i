def es_par(n:int) -> bool:
    ''' Requiere: nada.
        Devuelve: True si n es par, False si es impar.
    '''
    b:bool = (n % 2 == 0)
    return b

def describir_paridad(n:int) -> str:
    ''' Requiere: nada.
        Devuelve: "El número es par/impar", según corresponda.
    '''
    # Invocamos la función es_par, que devuelve True/False.
    # Obs: La expresión es_par(n) equivale a es_par(n)==True
    if es_par(n):
        return 'El número es par'
    else:
        return 'El número es impar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print(es_par(7))  # imprime: False
print(es_par(8))  # imprime: True

print(describir_paridad(7))  # imprime: El número es impar
print(describir_paridad(8))  # imprime: El número es par

