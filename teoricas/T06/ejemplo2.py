import math

def volumen_cilindro(r:float, h:float) -> float:
    ''' Requiere: r > 0, h > 0
        Devuelve: el volumen de un cilindro de radio r y altura h,
        calculado como pi*r*r*h, donde pi ~ 3.1415927
    '''
    v:float = math.pi * r * r * h
    return v

