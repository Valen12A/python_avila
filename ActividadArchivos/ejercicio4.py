#escriba un progrma que diga cuantas letras tine cada linea del coro del himno de shoacha 
#escriba la respuesta en otro archivo

try:
        file = open("ActividadArchivos/himno.txt", "r", encoding= "utf-8")
        linea=file.readlines()
        numLineas=len(linea)
        file = open("ActividadArchivos/himno.txt", "r")
        contenido = file.readline()
        numCaracteres = len(contenido)        
        cont = 1
        
        for line in file:
            file.readline()
            print(f" {numCaracteres} {line}")
            cont +=1
            print(f"El archivo contiene {numCaracteres} caracteres")
            print(f"El archivo tiene {numLineas} lineas")
            archivo = open("ActividadArchivos/himno1.txt", "a", encoding= "utf-8")
            num = [numCaracteres, numLineas]
            for i in num:
                archivo.write ( i + "\n")
            
        print(f"El archivo contiene {numCaracteres} caracteres")
        print(f"El archivo tiene {numLineas} lineas")
        
        file.close()

            
except IOError as e:
    print (e)