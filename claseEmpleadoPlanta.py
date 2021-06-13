from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldoBasico = 0.0
    __antiguedad = 0
    __sueldototal = 0.0 # A calcular
    def __init__(self,docu,nom,direc,tel,sueldoba,anti):
        super().__init__(docu, nom, direc, tel)
        if type(sueldoba) is float:
            self.__sueldoBasico = sueldoba
        if type(anti) is int:
            self.__antiguedad = anti
    def GetSueldoBasico(self):
        return self.__sueldoBasico
    def GetAntiguedad(self):
        return self.__antiguedad
    def GetSueldo(self): # Es el sueldo total
        self.__sueldototal = self.__sueldoBasico + ((self.__sueldoBasico * 1)/100) * self.__antiguedad
        return self.__sueldototal
    def SetSueldoBasico(self,nuevo):
        if type(nuevo) is float:
            self.__sueldoBasico = nuevo
            print('Se ha actualizado el sueldo basico.')