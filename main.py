from claseManejadorEmpleados import ManejadorEmpleados
from claseITesorero import ITesorero
from claseIGerente import IGerente

if __name__ == '__main__':
    me = ManejadorEmpleados()
    me.Carga()     
    print('Menu principal')
    print('1- Registrar horas.\n2- Total de tarea.\n3- Ayuda.\n4- Calcular sueldo.\n5- Ingreso a sistema con logeo de Tesorero/Gerente.\n0- Salir.')
    print('Opciones adicionales')
    print('6- Mostrar todo el archivo.')
    op = int(input('Seleccione opcion:'))
    while op != 0:
        if op == 1:
            me.RegistrarHoras()
        elif op == 2:
            me.TotalDeTarea()
        elif op == 3:
            me.Ayuda()
        elif op == 4:
            me.CalcularSueldo()
        elif op == 5:
            ban = False # Bandera validez de usuario/clave
            usuario = input('Ingrese usuario (uTesorero/uGerente):')
            clave = input('Ingrese contrasenha:')
            if usuario.lower() == 'uTesorero'.lower() and clave == 'ag@74ck':
                ban = True
                me.Tesorero(ITesorero(me))
            else:
                if usuario.lower() ==  'uGerente'.lower() and clave == 'ufC77#!1':
                    ban = True
                    me.Gerente(IGerente(me))
            if ban == False:
                print('Error. Usuario/Contrasenha incorrectas.')
        elif op == 0:
            print('Saliendo del programa.')
        elif op == 6: # Ahora opciones adicionales.
            me.MostrarTodos()
        print('Menu')
        print('1- Registrar horas.\n2- Total de tarea.\n3- Ayuda.\n4- Calcular sueldo.\n5- Ingreso a sistema con logeo de Tesorero/Gerente.\n0- Salir.')
        print('Opciones adicionales')
        print('6- Mostrar todo el archivo.')
        op = int(input('Seleccione opcion:'))
        
    # Seleccionar opcion 5 para usar el sistema de interfaces solicitado por la consigna