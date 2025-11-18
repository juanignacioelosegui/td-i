#justificacion nave_estelar_cercana

recordar:
nave_estelar_cercana(sensado:List[int], p:int) -> bool

##Terminación de algoritmo:

1. Se crean las variables i:int=0 y vr:bool=False
2. Luego entramos al ciclo el cual tiene como guarda/condición a i < len(sensado)   
3. En el cuerpo del ciclo tenemos un if y un incremento en 1 de i. En el cuerpo del if solamente se modifica la variable vr
4. Teniendo en cuenta que len(List) es siempre mayor o igual a cero, que i comienza en 0 para luego incrementarse de a 1 al final de cada iteración y que el tamaño de la lista sensado jamás es modificado, entonces podemos concluír en que en algún momento i será igual al tamaño de sensado, por lo que el ciclo finalizaría.
5. Por último solamente se devuelve la variable vr

##Correctitud del algoritmo:

recordar:
Requiere:  p>=0 y todos los sensado[i] >=0

Devuelve:  True si hay un elemento en sensado <= p entre las posiciones 0 e i-1 (incluídas)
            False en el caso contrario


En esta demo me voy a basar en el Requiere y el Devuelve
###Invariante:
1. 0 <= i <= len(sensado)
2.  True si hay un elemento en sensado <= p entre las posiciones 0 e i-1 (incluídas)
    False si no hay ningún elemento en sensado <= p entre las posiciones 0 e i-1 (incluídas)


Recordemos:
    i:int=0
    vr:bool=False
    #A
    while len(sensado) > i:
        
        #B
        if sensado[i] <= p:
            vr = True
        
        i=i+1
    	#C
    #D	
    return vr


Veamos que en (A) vale el inviariante pues 
1. i=0
2. vr = False entonces todos los elementos de sensado, entre la posición 0 a i-1, son mayores estrictos a p, veamos que esto último es cierto pues no hay elementos de sensado entre las posiciones 0 a -1 porque tenemos este rango vacío, es como si sensado=[] la lista vacía.

Ahora pueden pasar dos cosas, si no entramos al while entonces saltamos directamente a (D), si entramos al while es porque len(sensado)>0 entonces:

La primera vez que nos encontramos con (B) es la misma idea que en (A)

La primera vez que nos encontramos con (C), vemos que i=1 pues se incrementó en 1, y se analizó solamente el primer elemento de sensado entonces puede pasar que:
- vr=True entonces hay algún elemento de sensado, entre la posición 0 a 0, menor o igual a p, o sea que el primer elemento de sensado es menor o igual a p;  
- o sino, vr=False entonces todos los elementos de sensado, entre la posición 0 a 0, son mayores estrictos a p, o sea que el primer elemento de sensado es mayor estricto a p 

Luego repetimos (B) y (C) teniendo en cuenta que i se incrementa en 1 y en vr está el resultado de ver si hay algún elemento menor o igual a p entre las posiciones 0 a i-1, o sea, estoy analizando en cada iteración si cambia vr o no en base al elemento i-1 de sensado.

Luego de la última iteración del ciclo, vamos a incrementar en 1 a i de tal manera que i=len(sensado) y habremos analizado los elementos de sensado desde la posición 0 a la i-1 = len(sensado)-1.

Cuando estamos en (D) vale que i=len(sensado) y vr:

- vr=True entonces hay algún elemento de sensado, entre la posición 0 a len(sensado)-1, menor o igual a p;  
- o sino, vr=False entonces todos los elementos de sensado, entre la posición 0 a len(sensado)-1, son mayores estrictos a p, o sea que el primer elemento de sensado es mayor estricto a p 

Y esto hace que valga 'Devuelve', pues decir que analicé los elementos entre la posición 0 a len(sensado)-1 quiere decir que analicé todos los elementos, por lo que:

vr=True entonces hay algún elemento de sensado, entre la posición 0 a len(sensado)-1 (pues i=len(sensado)), menor o igual a p;  
o sino, vr=False entonces todos los elementos de sensado, entre la posición 0 a i-1, son mayores estrictos a p

Y esto es exactamente lo que pide Devuelve del algoritmo.
