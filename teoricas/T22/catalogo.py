from fruta import Fruta
from typing import List, TextIO, Set
import csv

class Catalogo:
    ''' Encapsula la entidad 'catalogo' de nuestra frutería online.
        Al crear un catalogo, se pasa un archivo CSV para leer las frutas.
        Un catalogo c tiene un atributo c.frutas de tipo List[Fruta] y
        un método c.frutas_de_estacion(est).
    '''
    
    def __init__(self, archivo_csv:str):
        '''
        Inicializa el catálogo de frutas, cargando las frutas contenidas
        en el archivo filename.
        Requiere: archivo_csv es el nombre de un archivo en formato
                  CSV (valores separados por comas), con tres columnas:
                  'nombre' (str), precio_por_kg (float), estaciones (lista de
                  strings separados por comas, donde los strings posibles son
                  'primavera', 'verano', 'otoño' o 'invierno').
        '''
        self.frutas:List[Fruta] = []
        f:TextIO = open(archivo_csv)
        for linea in csv.DictReader(f):
            nombre:str   = linea['nombre']
            precio:float = float(linea['precio_por_kg'])
            estaciones:Set[str] = set(linea['estaciones'].split(','))
            fru:Fruta = Fruta(nombre, precio, estaciones)
            self.frutas.append(fru)
        f.close()

    def frutas_de_estacion(self, estacion:str) -> List[Fruta]:
        '''
        Requiere: estacion es 'primavera', 'verano', 'otoño' o 'invierno'
        Devuelve: las frutas disponibles en la estación dada (en algún orden).
        '''
        vr:List[Fruta] = []
        for fru in self.frutas:
            if fru.disponible_en(estacion):
                vr.append(fru)
        return vr
