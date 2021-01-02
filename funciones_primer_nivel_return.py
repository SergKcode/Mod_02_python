

def maxi(*l)
    if len(l) == 0:
        return 0
    m=1[0]
    for indx in range (1,len(l)):
        if l[indx]>m:
            m =l [indx]
        return m

def mini (*l)
 if len(l) == 0:
        return 0
    m=1[0]
    for indx in range (1,len(l)):
        if l[indx]<m:
            m =l [indx]
        return m
    
def media (*l)
    if len(l)==0
        return 0
    suma=0
    for valor in l:
        suma += valor
    
    return suma/len(l)

funciones ={
    "max": maxi,
    "min": mini,
    "med": media
}


def returnF(nombre):
    nombre=nombre.lower
    if nombre in funciones.keys():
        return funciones [nombre]
    
    return None