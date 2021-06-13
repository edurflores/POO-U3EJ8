
class Empleado:
    __dni = ''
    __nombre = ''
    __direccion = ''
    __telefono = ''
    def __init__(self,docu,nom,direc,tel):
        self.__dni = docu
        self.__nombre = nom
        self.__direccion = direc
        self.__telefono = tel
    def GetDocu(self):
        return self.__dni
    def GetSueldo(self):
        pass
    def GetNombre(self):
        return self.__nombre
    def GetDireccion(self):
        return self.__direccion
    def GetTelefono(self):
        return self.__telefono