#suma, promedio, minimo, maximo, moda, desviasion estandar.
import random
import math
lista = []
suma = 0
menor= 0
mayor = 0
prom = 0
cont = 0 

tam = random.randint(10, 20)
print (tam)
for i in range (tam):
    num=random.randrange(100)
    lista.append(num)  
print (lista)

for  i in lista:
    suma = + suma + i
print ("la suma es: ", suma)


for i in range (len(lista)):
    suma += lista[i]
    prom = suma// (len (lista))
print ("el promedio es: ", prom)

for i in lista:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i
print ("el numero mayor es: ", mayor)
print ("el numero menor es:", menor)


max = 0
for numAct in lista:
    cont = 0
    for s in lista:
        if numAct == s:
            cont +=1
    if cont > max:
        max = cont 
        moda =numAct
print ("La moda es: ", moda )



for i in lista:
    resta = i - (suma/cont)
    cuadrado = resta (math.pow(2))
    suma += cuadrado
    division = suma / cont
raiz = math.sqrt(division)
print ( "La desviacion estandara es:", raiz)

