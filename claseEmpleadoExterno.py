from datetime import date
from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea = ''
    __fechainicio = date
    __fechafin = date
    __montoViatico = 0.0
    __costoObra = 0.0
    __montoSeguro = 0.0 # Monto de seguro de vida
    __sueldo = 0.0 # A calcular
    def __init__(self,docu,nom,direc,tel,tar,fechaini,fechafi,monviati,costo,monseguro):
        super().__init__(docu, nom, direc, tel)
        self.__tarea = tar
        self.__fechainicio = fechaini
        self.__fechafin = fechafi
        if type(monviati) is float:
            self.__montoViatico = monviati
        if type(costo) is float:
            self.__costoObra = costo
        if type(monseguro) is float:
            self.__montoSeguro = monseguro
        self.__sueldo = self.__costoObra - self.__montoViatico - self.__montoSeguro
    def GetTarea(self):
        return self.__tarea
    def GetSueldo(self):
        return self.__sueldo
    def GetFechaInicio(self):
        return self.__fechainicio
    def GetFechaFin(self):
        return self.__fechafin
    def GetMontoViatico(self):
        return self.__montoViatico
    def GetCostoObra(self):
        return self.__costoObra
    def GetMontoSeguro(self):
        return self.__montoSeguro
    def SetNuevoViatico(self,nuevo):
        if type(nuevo) is float:
            self.__montoViatico = nuevo
            print('Se ha actualizado el monto del viatico.')