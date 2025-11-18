from haversine import haversine, Unit      
from typing import Tuple

class Farmacia:
    def __init__(self, lat:float,lon:float, c_nom:str, c_alt:int, cp:str ,direc:str):
        '''Inicializa una farmacia con latitud lat, longitud lon, calle_nombre c_ nom , calle_altura c_alt, cpa cp, direccion direc'''
        self.latitud:float= lat                                                  # separamos longitud y latitud en 2 parametros ≠?
        self.longitud:float= lon
        self.calle_nombre:str= c_nom
        self.calle_altura:int= c_alt
        self.cpa:str= cp
        self.direccion:str= cp

    def distancia(self, lat_1:float, lng_1:float) -> float:                         
        ''' 
        Determina la distancia entre la farmacia mas cercana y el punto 
        Requiere: La coordenada de un punto conformado por un punto de latitud y otro de longitud, tipo float. 
        Devuelve: La distancia entre el punto y la farmacia; tipo float   ###DECRLE A CATA QUE ACA HAY QUE CORREGIR lo devuelve en lo que pida el usuario###
        '''
        punto_1:Tuple[float,float]= (lat_1, lng_1)
        punto_2:Tuple[float,float]= (self.latitud , self.longitud)                   #Aca hay un error de "lonigtud"                
        res: float=haversine(punto_1 , punto_2 , unit=Unit.METERS)                   #O(1)
        
        return res
        
    
    def __repr__(self) -> str:
        ''' Devuelve una representacion de tipo str del farmacia f'''
        return "FARMACIA: " + self.calle_nombre + str(self.calle_altura) + " ("+ self.cpa+ ")"     
#____________________

class Hospital:
    def __init__(self, lat:float,lon:float, h_nom:str, c_nom:str, c_alt:int, cp:str ,direc:str):
        '''  Inicializa un hospital h.latitud lat, h.longitud lon, h.nombre h_nom, h.calle_nombre c_nom, h.calle_altura c_alt, h.cpa cp, h.direccion direc '''
        self.latitud:float= lat                                 #Aca hay que cambiar lo de h.lat, h.lon,...#
        self.longitud:float= lon
        self.nombre: str= h_nom
        self.calle_nombre: str= c_nom
        self.calle_altura: int= c_alt
        self.cpa: str= cp
        self.direccion:str= direc        # No entiendo: "con el mismo formato que para las farmacias."
        
    
    def __repr__(self) -> str:
        '''  Devuelve una representacion de tipo str del hospital h '''
        return self.h_nombre + "--" + self.calle_nombre + str(self.calle_altura) + " ("+ self.cpa+ ")"     

#_________________________

import csv
from typing import Dict, List, TextIO
from farmacia import Farmacia
from hospital import Hospital


class DataSetSanitario:
    def __init__(self, filename_farmacias:str, filename_hospitales:str):
        ''' completar docstring '''
        self.farmacias: List[Farmacia] = []                                               
        self.hospitales: List[Hospital] = []    
        
        # Importamos las farmacias 
        file_farmacias: TextIO = open(filename_farmacias, 'r', encoding='utf-8')
        linea: Dict[str, str]                                                                   # esto se tiene que agregar?
        for linea in csv.DictReader(file_farmacias):                                     
            
            
            # Tomo los datos y los convierto a su respectivo tipo           
            longitud: float = float(linea['long'])                                                                 
            latitud: float = float(linea['lat']) 
            calle_nombre: str = linea['calle_nombre']
            calle_altura: int = int(linea['calle_altura'])
            cpa: str = linea['codigo_postal_argentino']
            
            #Crea un objeto de la clase Farmacia
            farmacia: Farmacia = Farmacia(longitud, latitud, f.calle_nombre, f.calle_altura, f.cpa)
            self. farmacias.append(farmacia)                                                  
        
        
        # Importamos los hospitales 
        file_hospitales: TextIO = open(filename_hospitales, 'r', encoding='utf-8')
        linea: Dict[str, str]                                                                   # ver
        for linea in csv.DictReader(file_hospitales):
            
            longitud:float = float(linea[WKT][0])
            latitud:float = float(linea[WKT][1]) 
            nombres:str= linea['NOM_MAP']
            calle_nombre:str= linea['CALLE']
            calle_altura: int= int(linea['ALTURA'])
            cpa: str= linea['COD_POSTAL']
            
            hospital: Hospital = Hospital(longitud, latitud, nombres, calle_nombre, calle_altura, cpa)
            self.farmacias.append(farmacia)       

        #Cerramos ambos archivos
        file_farmacias.close()
        file_hospitales.close()
        
    def nombres_de_hospitales(Farmacia) -> List [str]:
        ''' D: una lista con todos los hospitales ordenados alfabéticamente. '''
        n_de_hospitales: List [str]= [ ]
        for hospital in self.hospitales:  
            n_de_hospitales= (hospital.nombres).append
            return sort(n_de_hospitales)    
        
        
    def hospital_por_nombre(self) -> Hospital:                                                     # devuelve algo?
        ''' Dado el nombre (str) de un hospital(self), devuelve el objeto Hospital correspondiente.'''
        for hospital in self.hospitales:
            if hospital == hospital.nombres:                                                                                   # pq es constante? al estar acotado depende . podes asumir que un nombre del hospital no tienen infinitas letras, 
                return hospital


    #def farmacia_por_hospital() -> Dict [ Tuple[float, float],float ]: #metros ver si es float o int
        ''' 
        Devuelve un diccionario que asocia a cada hospital del dataset un par (o sea, una tupla) con la farmacia más cercana y la distancia a la misma (en metros).
        Es decir, las claves del diccionario deben ser objetos de tipo Hospital, y los valores, tuplas con un objeto de tipo Farmacia y un float.
        '''
        
       


    #def farmacia_mas_cercana(...) -> ...:
        ''' 
        Devuelve la farmacia del dataset d que está más cercana al hospital hosp. 
        '''
         

