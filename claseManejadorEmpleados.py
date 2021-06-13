import csv
import numpy as np
from datetime import date
from zope.interface import implementer
from claseEmpleado import Empleado
from claseEmpleadoPlanta import EmpleadoPlanta
from claseEmpleadoContratado import EmpleadoContratado
from claseEmpleadoExterno import EmpleadoExterno
from claseITesorero import ITesorero
from claseIGerente import IGerente

@implementer(ITesorero)
@implementer(IGerente)

class ManejadorEmpleados:
    __Manejador = None
    __arreEmpleados = None
    __dimension = 0
    __indice = 0
    def __init__(self):
        self.__arreEmpleados = np.empty(self.__dimension,dtype=Empleado)
    def AgregaEmpleado(self,unEmpleado):
        if isinstance(unEmpleado, Empleado):
            self.__dimension += 1
            self.__arreEmpleados.resize(self.__dimension)
            self.__arreEmpleados[self.__indice] = unEmpleado
            self.__indice += 1
    def CargaEmpPlanta(self):
        archivo = open('planta.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False:
                ban = True # Salta primera linea
            else:
                docu = fila[0]
                nom = fila[1]
                direc = fila[2]
                tel = fila[3]
                sueldoba = float(fila[4])
                anti = int(fila[5])
                unEmpleadoPlanta = EmpleadoPlanta(docu, nom, direc, tel, sueldoba, anti)
                self.AgregaEmpleado(unEmpleadoPlanta)
        archivo.close()
        print('Empleados de planta cargados.')
    def CargaEmpContratado(self):
        archivo = open('contratados.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False:
                ban = True # Salta primera linea
            else:
                docu = fila[0]
                nom = fila[1]
                direc = fila[2]
                tel = fila[3]
                auxfecha = fila[4].split('/')
                fechaini = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                auxfecha = fila[5].split('/')
                fechafin = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                cahoras = int(fila[6])
                unEmpleadoContratado = EmpleadoContratado(docu, nom, direc, tel, fechaini, fechafin, cahoras)
                self.AgregaEmpleado(unEmpleadoContratado)
        archivo.close()
        print('Empleados contratados cargados.')
    def CargaEmpExterno(self):
        archivo = open('externos.txt')
        reader = csv.reader(archivo, delimiter=',')
        ban = False
        for fila in reader:
            if ban == False:
                ban = True # Salta primera linea
            else:
                docu = fila[0]
                nom = fila[1]
                direc = fila[2]
                tel = fila[3]
                tar = fila[4]
                auxfecha = fila[5].split('/')
                fechaini = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                auxfecha = fila[6].split('/')
                fechafi = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                monviati = float(fila[7])
                costo = float(fila[8])
                monseguro = float(fila[9])
                unEmpleadoExterno = EmpleadoExterno(docu, nom, direc, tel, tar, fechaini, fechafi, monviati, costo, monseguro)
                self.AgregaEmpleado(unEmpleadoExterno)
        archivo.close()
        print('Empleados externos cargados.')
    def Carga(self):
        self.CargaEmpPlanta()
        self.CargaEmpContratado()
        self.CargaEmpExterno()
        print('Se han cargado todos los empleados.')
    def RegistrarHoras(self): # Consigna 1
        print('Funcion registrar horas.')
        docu = input('Ingrese DNI:')
        ban = False # Bandera para indicar si encontro al empleado.
        for i in range(self.__dimension):
            if self.__arreEmpleados[i].GetDocu() == docu:
                ban = True # Encontro al empleado.
                if isinstance(self.__arreEmpleados[i], EmpleadoContratado):
                    horas = int(input('Ingrese cantidad de horas trabajadas hoy:'))
                    self.__arreEmpleados[i].SetCantidadHoras(horas)
                    break
                else:
                    print('Error. El DNI proporcionado no corresponde a un empleado contratado.')
                    break
        if ban == False:
            print('Error. No se encontro empleado con el DNI proporcionado.')
    def TotalDeTarea(self): # Consigna 2 (falta considerar las fechas)
        print('Funcion total de tarea.')
        print('Seleccione tarea.\n1- Carpinteria.\n2- Electricidad.\n3- Plomeria.')
        op = int(input('Opcion:'))
        if op == 1:
            tarea = 'Carpinteria'
        elif op == 2:
            tarea = 'Electricidad'
        elif op == 3:
            tarea = 'Plomeria'
        total = 0.0 # Acumulador para calcular el monto total.
        fechaActual = date.today() # Fecha actual para determinar si hay tareas no finalizadas.
        for i in range(len(self.__arreEmpleados)):
            if isinstance(self.__arreEmpleados[i], EmpleadoExterno):
                if self.__arreEmpleados[i].GetTarea() == tarea:                  
                    if self.__arreEmpleados[i].GetFechaFin() > fechaActual: 
                        total += self.__arreEmpleados[i].GetSueldo()
        print('Monto total a pagar por la tarea {} : {}'.format(str(tarea),float(total)))
        print('--------------------------------------')
    def Ayuda(self): # Consigna 3
        print('Empleados que requieren la ayuda.')
        print('--------------------------------------')
        print('Nombre | Direccion | DNI')
        for i in range(len(self.__arreEmpleados)):
            if self.__arreEmpleados[i].GetSueldo() < 25000:
                print('{} | {} | {}'.format(str(self.__arreEmpleados[i].GetNombre()),str(self.__arreEmpleados[i].GetDireccion()),str(self.__arreEmpleados[i].GetDocu())))
    def CalcularSueldo(self): # Consigna 4
        print('Funcion calcular sueldos.')
        print('--------------------------------------')
        print('Nombre | Telefono | Sueldo a cobrar')
        print('--------------------------------------')
        for i in range(len(self.__arreEmpleados)):
            print('{} | {} | {}'.format(str(self.__arreEmpleados[i].GetNombre()),str(self.__arreEmpleados[i].GetTelefono()),float(self.__arreEmpleados[i].GetSueldo())))
        print('--------------------------------------')
    def MostrarTodos(self): # Opcional para ver toda la informacion del arreglo
        print('Todos los empleados.')
        for i in range(len(self.__arreEmpleados)):
            if isinstance(self.__arreEmpleados[i],EmpleadoContratado):
                print('Empleado contratado.')
                print('Nombre:',self.__arreEmpleados[i].GetNombre())
                print('DNI:',self.__arreEmpleados[i].GetDocu())
                print('Direccion:',self.__arreEmpleados[i].GetDireccion())
                print('Telefono:',self.__arreEmpleados[i].GetTelefono())
                print('Fecha de inicio:',self.__arreEmpleados[i].GetFechaInicio())
                print('Fecha de finalizacion:',self.__arreEmpleados[i].GetFechaFin())
                print('Cantidad de horas trabajadas:',self.__arreEmpleados[i].GetCantidadHoras())
                print('Sueldo:',self.__arreEmpleados[i].GetSueldo())
                print('Valor por hora:$',self.__arreEmpleados[i].GetValorHora())
                print('--------------------------------------')
            if isinstance(self.__arreEmpleados[i],EmpleadoPlanta):
                print('Empleado de planta.')
                print('Nombre:',self.__arreEmpleados[i].GetNombre())
                print('DNI:',self.__arreEmpleados[i].GetDocu())
                print('Direccion:',self.__arreEmpleados[i].GetDireccion())
                print('Telefono:',self.__arreEmpleados[i].GetTelefono())
                print('Sueldo basico:$',self.__arreEmpleados[i].GetSueldoBasico())
                print('Antiguedad:',self.__arreEmpleados[i].GetAntiguedad())
                print('Sueldo total:$',self.__arreEmpleados[i].GetSueldo())
                print('--------------------------------------')
            if isinstance(self.__arreEmpleados[i],EmpleadoExterno):
                print('Empleado externo.')
                print('Nombre:',self.__arreEmpleados[i].GetNombre())
                print('DNI:',self.__arreEmpleados[i].GetDocu())
                print('Direccion:',self.__arreEmpleados[i].GetDireccion())
                print('Telefono:',self.__arreEmpleados[i].GetTelefono())
                print('Tarea:',self.__arreEmpleados[i].GetTarea())
                print('Fecha de inicio:',self.__arreEmpleados[i].GetFechaInicio())
                print('Fecha de finalizacion:',self.__arreEmpleados[i].GetFechaFin())
                print('Monto de viatico:$',self.__arreEmpleados[i].GetMontoViatico())
                print('Costo de obra: $',self.__arreEmpleados[i].GetCostoObra())
                print('Monto de seguro de vida:$',self.__arreEmpleados[i].GetMontoSeguro())
                print('--------------------------------------')
    def ModificaValorHora(self):
        EmpleadoContratado.SetValorHora()
    # Ahora funciones para interfaces
    def gastosSueldoPorEmpleado(self,dni):
        ban = False # Bandera para indicar si encontro al empleado
        for i in range(len(self.__arreEmpleados)):
            if self.__arreEmpleados[i].GetDocu() == dni:
                ban = True # Encontro al empleado
                print('Nombre | Telefono | Gastos sueldo')
                print('--------------------------------------')
                print('{} | {} | {}'.format(str(self.__arreEmpleados[i].GetNombre()),str(self.__arreEmpleados[i].GetTelefono()),float(self.__arreEmpleados[i].GetSueldo())))
                break
        if ban == False:
            print('Error. No se encontro empleado con el DNI proporcionado.')
            
    def modificarBasicoEPlanta(self,dni,nuevoBasico):
        ban = False # Bandera para indicar si encontro al empleado
        for i in range(len(self.__arreEmpleados)):
            if self.__arreEmpleados[i].GetDocu() == dni:
                ban = True # Encontro al empleado
                if isinstance(self.__arreEmpleados[i],EmpleadoPlanta):
                    self.__arreEmpleados[i].SetSueldoBasico(nuevoBasico)
                    break
                else:
                    print('Error. El DNI proporcionado no corresponde al de un empleado de planta.')
                    break
        if ban == False:
            print('Error. No se encontro empleado con el DNI proporcionado.')
    
    def modificarViaticoEExterno(self,dni,nuevoViatico):
        ban = False # Bandera para indicar si encontro al empleado
        for i in range(len(self.__arreEmpleados)):
            if self.__arreEmpleados[i].GetDocu() == dni:
                ban = True # Encontro al empleado
                if isinstance(self.__arreEmpleados[i],EmpleadoExterno):
                    self.__arreEmpleados[i].SetNuevoViatico(nuevoViatico)
                    break
                else:
                    print('Error. El DNI proporcionado no corresponde al de un empleado externo.')
                    break
        if ban == False:
            print('Error. No se encontro empleado con el DNI proporcionado.')
            
    def modificarValorEPorHora(self,dni,nuevoValorHora):
        ban = False # Bandera para indicar si encontro al empleado
        for i in range(len(self.__arreEmpleados)):
            if self.__arreEmpleados[i].GetDocu() == dni:
                ban = True # Encontro al empleado
                if isinstance(self.__arreEmpleados[i],EmpleadoContratado):
                    self.__arreEmpleados[i].SetValorHora(nuevoValorHora)
                    break
                else:
                    print('Error. El DNI proporcionado no corresponde al de un empleado contratado.')
                    break
        if ban == False:
            print('Error. No se encontro empleado con el DNI proporcionado.')
    def Tesorero(self,manejadorTesorero):
        dni = input('Ingrese DNI del empleado:')
        self.gastosSueldoPorEmpleado(dni)
    def Gerente(self,manejadorGerente):
        print('Menu del gerente')
        print('1- Modificar sueldo basico (empleado de planta).\n2- Modificar monto de viatico (empleado externo).\n3- Modificar valor por hora (empleado contratado).')
        op = int(input('Seleccione opcion:'))
        if op == 1:
            dni = input('Ingrese DNI del empleado:')
            nuevo = float(input('Ingrese nuevo sueldo basico:'))
            self.modificarBasicoEPlanta(dni,nuevo)
        elif op == 2:
            dni = input('Ingrese DNI del empleado:')
            nuevo = float(input('Ingrese nuevo monto de viatico:'))
            self.modificarViaticoEExterno(dni,nuevo)
        elif op == 3:
            dni = input('Ingrese DNI del empleado:')
            nuevo = int(input('Ingrese nuevo valor por hora:'))
            self.modificarValorEPorHora(dni,nuevo)