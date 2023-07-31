from os import strerror

def crearArchivo (archivo): 
    try:
        file = open(archivo, "rt" )
        print ("El archivo ya exite")
        linea = file.readlines()
        numeroL = len(linea)
        print ("El numero de lines en el archivo es de: ", numeroL)
        file.close ()
        
    except FileNotFoundError:
        print("El archivo no exite ")
        try:
            file = open (archivo, "w")
            print ("Archivo creado")
        except IOError as e:
            print (f"Ocurrio un error{strerror(e.errno)}")
            
archivo=("C:\Vale\pythonavila\evaluacion\archivoTexto.txt")
            
            
    
        