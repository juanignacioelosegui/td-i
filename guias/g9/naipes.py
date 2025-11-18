from typing import List

class Naipe:
    def __init__(self, numero:int, palo:str):
        ''' Inicializa el naipe con el palo y numero dados.
            Requiere: numero es un entero entre 1 y 12 inclusive;
                 palo vale 'oros', 'copas', 'espadas' o 'bastos'. '''
        self.numero:int = numero
        self.palo:str   = palo

    def __repr__(self):
        ''' Representación str de un naipe. 
            Requiere: Nada. '''
        return str(self.numero) +' de '+self.palo

    def __lt__(self, other) -> bool:
        ''' Requiere: Nada.
            Devuelve: True sii un naipe viene antes que otro en el mazo,
                primero según el palo (oros < copas < espadas < bastos)
                y segundo según el número. '''
        p1:int = self.palo
        p2:int = other.palo
        return p1 < p2 or (p1 == p2 and self.numero < other.numero)

class Mazo:
    def __init__(self):
        ''' Inicializa el mazo sin ningún naipe. 
            Requiere: Nada.'''
        self.naipes:List[Naipe] = []

    def agregar(self, naipe:Naipe):
        ''' Agrega el naipe al mazo. 
            Requiere: Nada. '''
        self.naipes.append(naipe)

    def naipe_mas_alto(self) -> Naipe:
        ''' Requiere: hay al menos un naipe en el mazo. 
            Devuelve: el naipe más alto del mazo.'''
        vr:Naipe = self.naipes[0]
        for n in self.naipes:
            if vr < n:
                vr = n
        return vr

    def ordenar(self):
        ''' Ordena los naipes del mazo de menor a mayor. 
            Requiere: Nada. '''
        self.naipes.sort()

    def __repr__(self):
        ''' Representación str de un mazo de naipes. 
            Requiere: Nada. '''
        return str(self.naipes)

