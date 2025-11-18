from typing import Set,Dict

def caracteres(s:str) -> Set[str]:
    ''' Requiere: Nada.
        Devuelve: el conjunto de los caracteres que aparecen en s.
        Ejemplo: caracteres('bananas') --> {'b', 'a', 'n', 's'}
    '''
    conj:Set[str] = set()
    for caracter in s:
        conj.add(caracter)
    return conj

def caracteres_en_comun(s:str, t:str) -> Set[str]:
    ''' Requiere: Nada.
        Devuelve: el conjunto de los caracteres que aparecen tanto 
                  en s como en t.
        Ej: caracteres_en_comun('bananas', 'peras') --> {'a', 's'}
    '''
    return caracteres(s) & caracteres(t)

def recitar(n:int) -> str:
    ''' Requiere: n>=0.
        Devuelve: un string con la recitación en de los dígitos de n,
                  en minúsculas y separados por espacios en blanco.
        Ejemplos: recitar(1234) --> 'uno dos tres cuatro'
                  recitar(0)-->'cero'
                  recitar(999)-->'nueve nueve nueve'
    '''
    # Defino un diccionario que mapea dígitos a palabras.
    digito_a_palabra:Dict[str,str] = dict()
    digito_a_palabra['0'] = 'cero'
    digito_a_palabra['1'] = 'uno'
    digito_a_palabra['2'] = 'dos'
    digito_a_palabra['3'] = 'tres'
    digito_a_palabra['4'] = 'cuatro'
    digito_a_palabra['5'] = 'cinco'
    digito_a_palabra['6'] = 'seis'
    digito_a_palabra['7'] = 'siete'
    digito_a_palabra['8'] = 'ocho'
    digito_a_palabra['9'] = 'nueve'

    digitos:str = str(n)
    res:str = ''
    for d in digitos:
        res = res + digito_a_palabra[d] + ' '
    return res
     
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
