from typing import Set

PRI:str = 'primavera'
VER:str = 'verano'
OTO:str = 'otoño'
INV:str = 'invierno'

class Fruta:
    ''' Encapsula la entidad 'fruta' de nuestra frutería online.
        Una fruta f tiene atributos:
            - f.nombre (str)
            - f.precio (float)
            - f.estaciones (Set[str])
        y métodos:
            - f.disponible_en(estacion)
            - representación como string
            - menor que: <
    '''
    
    def __init__(self, n:str, p:float, es:Set[str]):
        ''' Inicializa una fruta con nombre n, precio p, estaciones es. '''
        self.nombre:str = n
        self.precio:float = p
        self.estaciones:Set[str] = es

    def disponible_en(self, estacion:str) -> bool:
        '''
        Requiere: estacion es 'primavera', 'verano', 'otoño' o 'invierno'
        Devuelve: True si estacion está en las estaciones de la fruta; False si no.
        '''
        return estacion in self.estaciones

    def __repr__(self) -> str:
        ''' Devuelve un string con los datos de la fruta.'''
        return self.nombre + ' ($' + str(self.precio) + '/kg)'

    def __lt__(self, other) -> bool:
        ''' Devuelve True si self < other; False en caso contrario.'''
        return self.precio < other.precio

