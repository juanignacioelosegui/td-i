def sumar_digitos(s:str) -> int:
    ''' 
    Requiere: s está formado solo por dígitos (0123456789).
    Devuelve: la suma de los dígitos de s.
    '''
    res:int = 0
    i:int = 0
    #A
    while i < len(s):
        #B
        res = res + int(s[i])
        i = i + 1
        #C
    #D
    return res

