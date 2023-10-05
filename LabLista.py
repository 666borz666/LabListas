#Creado por: Ignacio García y Daniel Campos
#Creación: 02/10/2023
#Ultima modificación: 05/10/2023
#Versión: 3.10.6
import re
recuperadosDonantes=["303500620","101110218","412340987","267893456","154328765","534561234","187674329","265437654","243214321","187654321","187659870","687659870","887659870","945659823"]
#Provincias
def buscarProvincia(registro):
    """
    Funcion: Hacer una busqueda por provincia 
    Entrada: registo
    Salida: Provincia
    """
    for provincia in registro[0]:
        if provincia == "1":
            provincia = "San José"
        elif provincia == "2":
            provincia = "Alajuela"
        elif provincia == "3":
            provincia = "Cartago"
        elif provincia == "4":
            provincia = "Heredia"
        elif provincia == "5":
            provincia = "Guanacaste"
        elif provincia == "6":
            provincia = "Puntarenas"
        elif provincia == "7":
            provincia = "Limón"
        elif provincia == "8":
            provincia = "Nacionalizados o naturalizados"
        elif provincia == "9":
            provincia = "Partida especial de nacimientos"
    return provincia
#1. 
def agregarDonadores(registro):
    """
    Función: Agregar los donares al BD
    Entrada: Registro
    Salida: registros de los donadores ingresado
    """
    if re.match(r'^\d{9}$', registro)==True:
        for pacienteReg in recuperadosDonantes:
            if registro == pacienteReg:
                print("¡La cedula ya esta registrada!")
            else:
                recuperadosDonantes.append(registro)
                print(f"Cedula {registro} registrada correctamente. ")
    else:
        print("La cédula no cumple con el formato correcto. Inténtelo de nuevo.")
        return
#2. 
def decodificarDonador(registro):
    """
    Función: Decoficar los donadores 
    Entrada: Registro
    Salida: Registro de decoficado
    """
    if re.match("\d{9}", registro):
        if registro in recuperadosDonantes:
            print(f"Usted es de {buscarProvincia(registro)} en el tomo {registro[1:5]} y asiento {registro[5:]}")
        else:
            print("El donador no es un donante aún.")
    else:
        print("La cédula no cumple con el formato correcto.")
#3
def listarDonadores(opcion):
    """
    Función: Generar una lista de donadores
    Entrada: Opcion()
    Salida: Lista segun los donadores
    """
    i = 0
    opcion=str(opcion)
    for pacienteReg in recuperadosDonantes:
        if pacienteReg[0]==opcion:
            print(pacienteReg)
            i += 1
        else:
            print("Aún no hay personas donadoras de esa naturalización")
            return
    print(f"Estos son los {i} donadores de la provincia {buscarProvincia(opcion)}.")
    return
#4
def donadoresTotales():
    """
    Función: Generar los donadores totales en la BD
    Entrada: total
    Salida: Todos los donadores del clorito picado
    """
    recuperadosDonantes.sort() 
    a = b = c = d = e = f = g = h = i = 0
    for pacienteReg in recuperadosDonantes:
        if pacienteReg[0]=="1":
            a += 1
            print(pacienteReg)
        if pacienteReg[0]=="2":
            b += 1
            print(pacienteReg)
        if pacienteReg[0]=="3":
            c += 1
            print(pacienteReg)
        if pacienteReg[0]=="4":
            d += 1
            print(pacienteReg)
        if pacienteReg[0]=="5":
            e += 1
            print(pacienteReg)
        if pacienteReg[0]=="6":
            f += 1
            print(pacienteReg)
        if pacienteReg[0]=="7":
            g += 1
            print(pacienteReg)
        if pacienteReg[0]=="8":
            h += 1
            print(pacienteReg)
        if pacienteReg[0]=="9":
            i += 1
            print(pacienteReg)
    print(f"Los donadores de San José son {a} con las cédulas mostradas.")
    print(f"Los donadores de Alajuela son {b} con las cédulas mostradas.")
    print(f"Los donadores de Cartago son {c} con las cédulas mostradas.")
    print(f"Los donadores de Heredia son {d} con las cédulas mostradas.")
    print(f"Los donadores de Guanacaste son {e} con las cédulas mostradas.")
    print(f"Los donadores de Puntarenas son {f} con las cédulas mostradas.")
    print(f"Los donadores de Limón son {g} con las cédulas mostradas.")
    print(f"Los donadores nacionalizados o naturalizados son {h} con las cédulas mostradas.")
    print(f"Los donadores con partida especial de nacimiento son {i} con las cédulas mostradas.")
    return
#5
def donadoresNoTipicos():
    """
    Función: Donadores no a tipico de la BD
    Entrada: pacientes
    Salida: muestra la posible lsita de donadores tipicos
    """
    i = 0
    j = 0
    for pacienteReg in recuperadosDonantes:
        if pacienteReg[0]=="8":
            print("Nacionalizados o naturalizados:")
            i += 1
            print(pacienteReg)
        elif pacienteReg[0]=="9":
            print("Partida especial de nacimientos:")
            j += 1
            print(pacienteReg)
    print(f"Los donadores nacionalizados o naturalizados, son {i} con las cédulas mostradas.")
    print(f"Los donadores con partida especial de nacimiento, son {j} con las cédulas mostradas.")
    return