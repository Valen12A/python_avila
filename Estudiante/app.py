from Estudiante import *
import csv

estudiantes = []
with open ("C:\Users\Aprendiz\Downloads") as file:
    csvReader=csv.reader(file)
for row in csvReader:
        
    objeto = estudiantes(row[0],row[1],row[2],row[3])
    print(objeto.verDatos())
    estudiantes.append(objeto)