class empleado :
    def __init__ (self, nombre, cargo , salario):
        self.__nombre=nombre 
        self.__cargo=cargo
        self.__salario=salario
        
    def getNombre(self):  
        return self.__nombre
    def setNombre (self, nombre):
        self.__nombre=nombre
        
    
    def getCargo(self):  
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo= cargo
        
    
p1=empleado("María")

print (p1.getNombre())
p1=empleado ("Conductora")
print (p1.getCargo())



