from typing import Set, Dict
from fruta import Fruta

class Carrito:
    ''' Encapsula la entidad 'carrito de compras' de nuestra frutería online.
        Un carrito c debe usarse mediante estos métodos:
            - c.agregar(fruta, peso)
            - c.sacar(fruta, peso)
            - c.calcular_precio_total()
            - c.frutas_en_carrito()
            - c.kilos_de_fruta()
        Nunca modificar los atributos c.kg_fruta y c.precio_total
        directamente, para evitar romper la consistencia de los mismos.
    '''
    
    def __init__(self):
        '''
        Inicializa un carrito vacío.
        Requiere: nada.
        '''
        self.kg_fruta:Dict[Fruta, int] = dict()
        self.precio_total = 0

    def __repr__(self) -> str:
        ''' 
        Devuelve un string con los datos del carrito. 
        Requiere: Nada
        '''
        return str(self.kg_fruta)

    def agregar(self, f:Fruta, p:int):
        '''
        Modifica: Agrega p kilos de la fruta f al carrito.
        Requiere: p>0.
        '''
        if f in self.kg_fruta:
            self.kg_fruta[f] = self.kg_fruta[f] + p
        else:
            self.kg_fruta[f] = p
        self.precio_total = self.precio_total + f.precio * p

    def sacar(self, f:Fruta, p:int):
        '''
        Modifica: Saca p kilos de la fruta f del carrito.
        Requiere: p>0, y hay al menos p kilos de f.
        '''
        self.kg_fruta[f] = self.kg_fruta[f] - p
        if self.kg_fruta[f] == 0:
            self.kg_fruta.pop(f)
        self.precio_total = self.precio_total - f.precio * p

    def calcular_precio_total(self) -> float:
        '''
        Requiere: nada
        Devuelve: el precio de total de todo lo que hay en el carrito.
        '''
        return self.precio_total

    def frutas_en_carrito(self) -> Set[Fruta]:
        '''
        Requiere: nada.
        Devuelve: el conjunto de frutas que hay en el carrito
                  (solo las frutas, sin sus cantidades).
        '''
        return set(self.kg_fruta.keys())

    def kilos_de_fruta(self, f:Fruta) -> int:
        '''
        Requiere: nada.
        Devuelve: la cantidad de kg de f en el carrito.
        '''
        if f in self.kg_fruta:
            return self.kg_fruta[f]
        else:
            return 0
