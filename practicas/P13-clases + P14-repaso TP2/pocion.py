from typing import List

class Pocion:
    ''' Representa una poción del universo de Harry Potter.
        Una poción p tiene atributos:
            - p.nombre (str)
            - p.ingredientes_conocidos (List[str])
            - p.efecto (str)
            - p.caracteristicas (str)
            - p.nivel_dificultad (str)
        y métodos:
            - representación como string
            - menor que: <
    '''
    def __init__(self, n:str, ic:List[str], e:str, c:str, nd:str):
        '''
        Inicializa una poción con nombre n, ingredientes secretos ic,
        efecto e, características c y nivel_dificultad nd.
        Requiere: nada.
        '''

        # .... completar ....
    
    
    def __repr__(self) -> str:
        '''
        Genera la representación de una poción como string.
        Requiere: nada.
        Devuelve: el string que representa con el nombre de la poción.
        '''
        # .... completar ....
        

    def __lt__(self, other) -> bool:
        '''
        Relación self < other, basada en el orden lexicográfico del nombre
        de las pociones.
        Requiere: nada.
        Devuelve: True si el nombre de self es menor que el de other de acuerdo
                  al orden lexicográfico; False en caso contrario.
        '''
        # .... completar ....
