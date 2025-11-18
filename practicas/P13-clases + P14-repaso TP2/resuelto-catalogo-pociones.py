from pocion import Pocion
from typing import Dict, Set, List, Tuple, TextIO
import csv

class CatalogoPociones:
    def __init__(self, archivo_csv:str):
        '''
        Inicializa el catálogo de pociones, cargando las pociones
        contenidas en el archivo archivo_csv que tienen el nivel de
        dificultad definido (el resto las ignora).
        Requiere: archivo_csv es el nombre de un archivo en formato
                  CSV (valores separados por punto y coma), con cinco columnas:
                  'Name' (str), 'Known ingredients' (lista de
                  strings separados por comas), 'Effect' (str),
                  'Characteristics' (str), 'Difficulty level' (str).
        '''
        self.pociones_dificultad:Dict[str, Set[Pocion]] = dict()
        f:TextIO = open(archivo_csv)
        for linea in csv.DictReader(f, delimiter=';'):
            nd:str = linea['Difficulty level']
            if nd != '':
                nom:str = linea['Name']
                ing:List[str] = linea['Known ingredients'].split(',')
                for i in range(len(ing)):
                    ing[i] = ing[i].strip()                
                ef:str = linea['Effect']
                car:str = linea['Characteristics']
                p:Pocion = Pocion(nom, ing, ef, car, nd)
                if nd not in self.pociones_dificultad:
                    self.pociones_dificultad[nd] = set()
                self.pociones_dificultad[nd].add(p)
        f.close()

    def __repr__(self):
        '''
        Genera la representación de una catálogo de pociones como string.
        Requiere: nada.
        Devuelve: el string que representa al catálogo.
        '''
        return str(self.pociones_dificultad)

    def listar_por_dificultad(self, dif:str) -> List[Pocion]:
        '''
        Requiere: nada
        Devuelve: una lista de Pociones, donde dif
        correposnde a una cierta dificultad recibida como argumento que se corresponde
        con la dificultad de las pociones que se deben guardar en la lista de salida.
        Por ejemplo, si el método se invoca con el argumento 'Advanced', la lista contendrá
        pociones de tipo Advance.
        Además, en la lista las pociones aparecen
        ordenadas de acuerdo al orden definido en la clase Pocion.
        '''

        pociones:List[Pocion] = list(self.pociones_dificultad[dif])
        pociones.sort()
        return pociones

    def listar_pociones_con_n_ingredientes(self, n:int) -> List[Tuple[str,Pocion]]:
        '''
        Requiere: n > 0
        Devuelve: una lista de tuplas dónde cada tupla almacena una poción y su dificultad.
        Las pociones que conforman las tuplas de la listas son aquellas que tienen n ingredientes.
        '''
        
        res: List[Tuple[str,Pocion]] = []
        for dif in self.pociones_dificultad:
            pociones = self.pociones_dificultad[dif]
            for p in pociones:
                if len(p.ingredientes_conocidos)== n:
                    res.append((dif,p))
        return res

c = CatalogoPociones('Potions-mini.csv')
print(c.listar_por_dificultad('Advanced'))
print(c.listar_por_dificultad('Beginner'))
print(c.listar_pociones_con_n_ingredientes(3))
print(c.listar_pociones_con_n_ingredientes(1))

