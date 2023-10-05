#Creado por: Ignacio García y Daniel Campos
#Creación: 02/10/2023
#Ultima modificación: 05/10/2023
#Versión: 3.10.6
#Importación de librerias
from LabLista import *
#Definición de funciones
def opcionagregarDonadores():
    """
    Función: Agregar los posibles donadores. 
    Entrada: Cedula con 9 digitos.
    Salida: No tiene salida directa, pero realiza el registro del donador y retorna al menú principal.
    """
    registro=input("Ingrese una cédula (9 digitos numericos): ")
    agregarDonadores(registro)
    return menu()

def opciondecodificarDonador():
    """
    Función: Codificar los donadores.
    Entrada: Cedula con 9 digitos
    Salida: No tiene salida directa, pero realiza el registro del donador y retorna al menú principal.
    """
    registro=input("Ingrese una cédula (9 digitos numericos): ")
    decodificarDonador(registro)
    return menu()

def opcionlistarDonadores():
    """
    Función: Lista de donares por provincias
    Entrada: Numero de provincia a bucar
    Salida: No tiene salida directa, pero realiza el registro del donador y retorna al menú principal.
    """
    try:
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
    except ValueError:
        print("La opción ingresada no es válida. Inténtelo de nuevo.")
    return menu()

def opciondonadoresTotales():
    """
    Función: Donadores totales en la BD.
    Entrada: Donadores
    Salida: No tiene salida directa, pero realiza el registro del donador y retorna al menú principal.
    """
    donadoresTotales()
    return menu()

def opciondonadoresNoTipicos():
    """
    Función: Donadores no a tipicos 
    Entrada: Donadores
    Salida: No tiene salida directa, pero realiza el registro del donador y retorna al menú principal.
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