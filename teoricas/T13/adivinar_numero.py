import random

def adivinar_numero(numero:int):
    ''' Pide al usuario que adivine el número ingresado, hasta acertarle.
        Requiere: 1 <= numero <= 5
        Devuelve: Nada.
    '''
    listo:bool = False
    cantidad_intentos:int = 0
    while not listo:
        mensaje:str = 'Adiviná en qué número del 1 al 5 estoy pensando: '
        intento:int = int(input(mensaje))
        cantidad_intentos = cantidad_intentos + 1
        if intento == numero:
            listo = True
        else:
            print('Nop')
    print('Bien! Adivinaste en '+str(cantidad_intentos)+' intento/s.')


# Elijo un número al azar.
numero_secreto:int = random.randint(1,5)

# Empiezo a jugar.
adivinar_numero(numero_secreto)
