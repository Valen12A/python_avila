class persona:
    def __init__ (self, nombre, documento,):
        self.__nombre =nombre 
        self.__documento=documento
        self.__curso  = []
    
    def getNombre(self):
        return self.__nombre
    def setNombre (self, nombre):
        self.__nombre= nombre
    
    def getDocumento(self):
        return self.__documento
    def setDocumento (self, documento):
        self.__documento= documento
        
    def añadirCursos(self, curso):
        self.__curso += [curso]
    def getCursos(self):
        return self.__curso
    
    def buscarCurso(self, curso):
        if curso in self.__curso:
            return ("El curso si esta en la lista.")
        else:
            return ("El curso no esta en la lista de cursos.")
    
    def eliminarCurso(self, Curso):
        if Curso in self.__curso:
            self.__curso.remove(Curso)
            return ("El curso fue eliminado")
        else:
            return ("El curso no se puede eliminar ya que no esta en la lista.")
        
        
    def modificarCurso(self, curso, n_curso):
        Cont = 0
        for x in range(len(self.__curso)):
            Cont+=1
            if self.__curso[x] == curso:
                self.__curso[Cont-1] = n_curso
            if self.__curso[x] == self.__curso[-1]:
                self.__curso[-1] = n_curso
    
p= persona("ana", 123)
print(p.getNombre())

p= persona("ana", 123)
print(p.getDocumento())

q= persona ("pedro", 321)
print(q.getNombre())


q= persona ("pedro", 321)
print(q.getDocumento())
 
p.añadir.Curso("matematicas")
p.añadir.Curso("sociales")
p.añadir.Curso("ingles")
p.añadir.Curso("biologia")

print(p.anadirCuso())



