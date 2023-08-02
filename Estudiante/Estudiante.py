class Estudiante:
    def __init__(self,codIcfes, documento, fechaNacimiento, codMunicipio,):
        self.__codIcfes = codIcfes
        self.__documento = documento
        self.__fechaNacimiento = fechaNacimiento
        self.__codMunicipio = codMunicipio
        
        
        
    def datos (self):
        return f"{self.__documento, self.__codIcfes, self.__fechaNacimiento, self.__codMunicipio}"
    
    