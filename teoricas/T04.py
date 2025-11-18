def millas_a_kilometros(d:float) -> float:
    ''' Requiere: d >= 0 
        Devuelve: el resultado (aproximado) de convertir d de millas
        a kilómetros, sabiendo que 1 mi ~ 1.60934 km. 
    '''
    res:float = d * 1.60934
    return res

# Cuerpo principal del programa
mi:float = 123.4
km:float = millas_a_kilometros(mi)
mensaje:str = str(int(mi))+" millas equivale a "+str(int(km))+" kilómetros."
print(mensaje)
