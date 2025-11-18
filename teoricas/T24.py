import turtle as t

t.shape("turtle")
t.speed(0)

def triangulo(d:float):
    ''' Requiere: d>0
        Devuelve: nada
        Dibuja un triángulo equilátero de lado d. '''
    for i in range(3):
        t.forward(d)
        t.left(120)

#triangulo(100)
    
def lineas_punteadas(n:int, d:float):
    ''' Requiere: d>0, n>=0
        Devuelve: nada
        Dibuja n líneas punteadas de longitud d. '''
    for i in range(n):
        t.pendown()
        t.forward(d) # dibujo
        t.penup()
        t.forward(d) # no dibujo

#lineas_punteadas(20, 5)

def cuadrado(d:float):
    ''' Requiere: d>0
        Devuelve: nada
        Dibuja un cuadrado de lado d. '''
    for i in range(4):
        t.forward(d)
        t.left(90)

#cuadrado(100)

def escalera(d:float, n:int):
    ''' Requiere: d>0, n>=0.
        Devuelve: nada
        Dibuja una escalera con n escalones de tamaño d. '''
    if n==0:    # caso base
        pass
    else:       # caso recursivo
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.right(90)
        escalera(d, n-1)

#escalera(20, 10)

def escalera2(d:float, k:float):
    ''' Requiere: k>0
        Devuelve: nada
        Dibuja una escalera con escalones de tamaño d, d-k, d-2k, ...,'''
    if d <= 0:    # caso base
        pass
    else:         # caso recursivo
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.right(90)
        escalera2(d-k, k)

#escalera2(20, 1)

def espiral_cuadrada(d:float, k:float):
    ''' Requiere: k>0
        Devuelve: nada
        Dibuja una espiral cuadrada con lados de largo d, d-k, d-2k, ... '''
    if d <= 0:    # caso base
        pass
    else:         # caso recursivo
        t.forward(d)
        t.left(90)
        espiral_cuadrada(d-k, k)

#espiral_cuadrada(200, 3)

def montaña(d:float):
    ''' Requiere: d>0
        Devuelve: nada
        Dibuja una montaña simple de largo d. '''
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)
    t.right(120)
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)

#montaña(300)

def montaña_recursiva(d:float):
    ''' Requiere: d>0
        Devuelve: nada
        Dibuja una curva de Koch de largo d. '''
    if d<5:      # caso base
        t.forward(d)
    else:        # caso recursivo
        montaña_recursiva(d/3)
        t.left(60)
        montaña_recursiva(d/3)
        t.right(120)
        montaña_recursiva(d/3)
        t.left(60)
        montaña_recursiva(d/3)

#montaña_recursiva(300)

def copo_nieve_koch(d:float):
    ''' Requiere: d>0
        Devuelve: nada
        Dibuja un copo de nieve de Koch de lado d. '''
    for i in range(3):
        montaña_recursiva(d)
        t.right(120)
        
#copo_nieve_koch(300)
        
t.mainloop()
t.bye()
