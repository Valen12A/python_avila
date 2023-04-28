
suma = 0
resta =0
for i in range (1,1000 + 1):
    if resta == i:
        print(f"El numero {h} es perfecto") 
    for h in range (1000):
        if h %  i ==0:
            suma+=i
        resta = suma - h
        