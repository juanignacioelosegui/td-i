def cant_vocales(txt:str) -> int:
    ''' Requiere: txt está formado solo por los caracteres
           ,.;:¿?¡!-'", aábcdeéfghiíjklmnñoópqrstuúüvwxyz, 
           sus mayúsculas y espacios en blanco.
        Devuelve: la cantidad de apariciones en txt de los
           caracteres aáeéiíoóuúü y sus mayúsculas.
    '''
    VOCALES:str = 'aeiouAEIOUáéíóúüÁÉÍÓÚÜ'
    cant:int = 0
    i:int = 0
    while i<len(txt):
        if txt[i] in VOCALES:
            cant = cant + 1
        i = i + 1
    return cant

