#Creado por: Ignacio García y Daniel Campos
#Creación: 02/10/2023
#Ultima modificación: 
#Versión: 3.10.6
#Importación de librerias
from LabLista import *
#Definición de funciones
def opcionagregarDonadores():
    """
    Función:
    Entrada:
    Salida:
    """
    registro=input("Ingrese una cédula (9 digitos numericos): ")
    agregarDonadores(registro)
    return menu()

def opciondecodificarDonador():
    """
    Función:
    Entrada:
    Salida:
    """
    registro=input("Ingrese una cédula (9 digitos numericos): ")
    decodificarDonador(registro)
    return menu()

def opcionlistarDonadores():
    """
    Función:
    Entrada:
    Salida:
    """
    print("1. San José")
    print("2. Alajuela")
    print("3. Cartago")
    print("4. Heredia")
    print("5. Guanacaste")
    print("6. Puntarenas")
    print("7. Limón")
    print("8. Nacionalizados o naturalizados")
    print("9. Partida especial de nacimientos")
    opcion=input("Ingrese la provincia que desea listar: ")
    listarDonadores(opcion)
    return menu()

def opciondonadoresTotales():
    """
    Función:
    Entrada:
    Salida:
    """
    donadoresTotales()
    return menu()

def opciondonadoresNoTipicos():
    """
    Función:
    Entrada:
    Salida:
    """
    donadoresNoTipicos()
    return menu()

#Menú
def menu():
    print("**************************************")
    print("Bienvenido al sistema de donaciones.")
    print("1. Agregar convalecientes donadores del día")
    print("2. Decodificar donador.")
    print("3. Listar donadores según el Registro de Naturalizaciones.")
    print("4. Donadores totales del país.")
    print("5. Donadores no típicos")
    print("6. Salir")
    print("**************************************")
    try:
        opcion=int(input("Indique la opción que desea: "))
        if opcion == 1:
            print(opcionagregarDonadores())
        elif opcion == 2:
            print(opciondecodificarDonador())
        elif opcion == 3:
            print(opcionlistarDonadores())
        elif opcion == 4:
            print(opciondonadoresTotales())
        elif opcion == 5:
            print(opciondonadoresNoTipicos())
        elif opcion == 6:
            print("Gracias por utilizar el sistema.")
            return ""
    except ValueError:
        print("La opción ingresada no es válida. Inténtelo de nuevo.")
        menu()
#Programa principal
menu()