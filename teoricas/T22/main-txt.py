# Este programa implementa una interfaz interactiva en modo texto.
# Permite realizar las siguientes operaciones:
# - ver el estado actual del carrito de compras;
# - agregar una cantidad de kilos de una fruta al carrito.
# - sacar una cantidad de kilos de una fruta del carrito.
# - calcular el precio actual del carrito.
# - terminar.

from typing import List
from fruta import Fruta
from carrito import Carrito
from catalogo import Catalogo
from datetime import date

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def estacion_actual() -> str:
    ''' Devuelve la estación de la fecha de hoy. El valor de retorno 
        es uno de 'primavera', 'verano', 'otoño' o 'invierno'.  '''
    today:date = date.today()
    empieza_otoño:date     = date(today.year, 3, 21)  # 21 de marzo
    empieza_invierno:date  = date(today.year, 6, 21)  # 21 de junio
    empieza_primavera:date = date(today.year, 9, 21)  # 21 de junio
    empieza_verano:date    = date(today.year, 12, 21) # 21 de diciembre
    vr:str
    if today >= empieza_verano:
        vr = 'verano'
    elif today >= empieza_primavera:
        vr = 'primavera'
    elif today >= empieza_invierno:
        vr = 'invierno'
    elif today >= empieza_otoño:
        vr = 'otoño'
    else:
        vr = 'verano'
    return vr

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def imprimir_carrito(c:Carrito):
    ''' Imprime por pantalla la lista de frutas del carrito, 
        ordenadas por precio de menor a mayor. '''
    i:int = 0
    frutas:List[Fruta] = list(c.frutas_en_carrito())
    frutas.sort()
    if len(frutas) == 0:
        print('El carrito de compras está vacío.')
    else:
        print('Carrito de compras:')
        while i < len(frutas):
            kg:int = c.kilos_de_fruta(frutas[i])
            print(i+1, frutas[i], '-->', kg, 'kilogramos')
            i = i + 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def imprimir_lista_de_frutas(frutas:List[Fruta]):
    ''' Imprime por pantalla la lista de frutas numeradas (1,2,3,...). '''
    print('Frutas disponibles:')
    i:int = 0
    while i < len(frutas_disponibles):
        print(i+1, frutas_disponibles[i])
        i = i + 1        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Creamos un carrito nuevo para el usuario actual.
carrito:Carrito = Carrito()

# Cargamos el catálogo de frutas de un archivo CSV.
catalogo:Catalogo = Catalogo('frutas.csv')

# Nos quedamos solamente con las frutas que están disponibles ahora.
frutas_disponibles:List[Fruta] = catalogo.frutas_de_estacion(estacion_actual())

# Ciclo principal de la interfaz interactiva.
terminamos:bool = False
while not terminamos:
    print('Comandos: [v]er carrito, [a]gregar, [s]acar, [p]recio, [t]erminar')
    comando:str = input('Ingrese su comando: ')
 
    # ver carrito - - - - - - - - - - - - - - - - - - - - - - - - - -
    if comando=='v':
        imprimir_carrito(carrito)
    
    # agregar fruta al carrito - - - - - - - - - - - - - - - - - - - -
    elif comando=='a': 
        imprimir_lista_de_frutas(frutas_disponibles)
        num:int = int(input('Ingrese el número de fruta que desea agregar, o 0 para cancelar: '))
        if num>0:
            kg:int = int(input('Ingrese la cantidad de kg a agregar: '))
            # Revisamos que (num,kg) ingresados tengan sentido.
            if kg>0 and num<=len(frutas_disponibles):
                carrito.agregar(frutas_disponibles[num-1], kg)
            else:
                print('El valor ingresado es inválido.')

    # sacar fruta del carrito - - - - - - - - - - - - - - - - - - - -
    elif comando=='s':
        imprimir_carrito(carrito)
        num:int = int(input('Ingrese el número de fruta que desea sacar, o 0 para cancelar: '))
        if num>0:
            frutas:List[Fruta] = list(carrito.frutas_en_carrito())
            frutas.sort()
            kg:int = int(input('Ingrese la cantidad de kg a sacar: '))
            # Revisamos que (num,kg) ingresados tengan sentido.
            if num<=len(frutas) and 0<kg<=carrito.kilos_de_fruta(frutas[num-1]):
                carrito.sacar(frutas[num-1], kg)
            else:
                print('El valor ingresado es inválido.')

    # calcular precio actual - - - - - - - - - - - - - - - - - - - - -
    elif comando=='p':
        precio:float = carrito.calcular_precio_total()
        print("Precio actual del carrito: $ %.2f" % precio)

    # terminar - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    elif comando=='t':
        terminamos = True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
