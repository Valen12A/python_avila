numero = int (input("ingrese bun numero"))

for i in range (1, 100 +1): 
    if numero %  i ==0:
        print("el numero ", i , "es divisor de",numero  )