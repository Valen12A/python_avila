# Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del programa.

def fib (x):
    num1 =0
    num2 =1

    for j in range (x):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    
    return num2

lista = []
num=int(input ("Ingrese la cantidad que quier ever de la serie de fibonacci: "))


for i in range (num):
    lista.append(fib(i))

print(lista) 


