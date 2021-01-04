from functools import reduce


def doble (x):
    return x+x

lista=[1,3,-1,15,9]

listaDobles=map (lambda x:x*2)
listaDobles= map(doble,lista)

def esPar(x):
    return x%2==0


listaPares1= filter(esPar,lista)
listaPares =filter(lambda x: x%2==0, lista)

sumatorio= reduce(lambda x, y: x+y,lista)
sumatorioDobles= reduce(lambda x, y: x+y*2,lista)


suma100 =reduce(lambda x,y:x+y, range (101)) 

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)