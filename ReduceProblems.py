from functools import reduce


def doble (x):
    return x+x

def SumatorioClasico(l):
    resultado=0
    for valor in l:
        resultado +=valor
        
    return resultado
    
def SumatorioDobleClasico(l):
    resultado=0
    for valir in l:
        resultado += valor*2
    return resultado

def ProductoTotal(l):
    resultado=1
    for valor in l:
        resultado*=valor
    retun resultado

lista=[1,3,-1,15,9]

listaDobles=map (lambda x:x*2)
listaDobles= map(doble,lista)

def esPar(x):
    return x%2==0


listaPares1= filter(esPar,lista)
listaPares =filter(lambda x: x%2==0, lista)

suma100 =reduce(lambda x,y:x+y, range (101)) 



sumatorio= reduce(lambda x, y: x+y,lista)

l=lista [:]
l.insert(0,0) 
sumatorioDobles= reduce(lambda x, y: x+y*2,l)

print (sumatorio)
print (sumatorioDobles)
