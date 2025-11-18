from typing import List #importante import para que listas ande bien

def nave_estelar_cercana(sensado:List[int], p:int) -> bool:
    
    """
    Requiere:  p >= 0 and los elementos de la lista sensado sean >= 0
	Devuelve:  True si hay un elemento en sensado <= p
                False en el caso contrario
    """
    vr:bool = False
    i:int = 0
    
    while (i <= len(sensado) - 1): #equivalente i < len(sensado)
        
        if sensado[i] <= p:
            vr= True
        
        i=i+1
    
    return vr



