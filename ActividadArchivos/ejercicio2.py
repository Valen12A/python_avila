try:
        file = open("ActividadArchivos/himno.txt", "r", encoding= "utf-8")
        cont = 1
        for line in file:
            file.readline()
            print(f"{cont} {line}")
            cont +=1
        file.close()
except IOError as e:
    print(e)