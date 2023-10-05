#Creado por: Ignacio García y Daniel Campos
#Creación: 02/10/2023
#Ultima modificación: 
#Versión: 3.10.6
import re
recuperadosDonantes=["303500620","101110218","412340987","267893456","154328765","534561234","187674329","265437654","243214321","187654321","187659870","687659870","887659870","945659823"]
#1. 
def agregarDonadores(registro):
    """
    Función:
    Entrada:
    Salida:
    """
    if re.match("\d{9}", registro)==True:
        for pacienteReg in recuperadosDonantes:
            if registro == pacienteReg:
                print("¡La cedula ya esta registrada!")
            else:
                recuperadosDonantes.append(registro)
                print(f"Cedula{registro} registrada correctamente. ")
    else:
        print("La cédula no cumple con el formato correcto. Inténtelo de nuevo.")
        return
#2. 
def decodificarDonador(registro):
    """
    Función:
    Entrada:
    Salida:
    """
    if re.match("\d{9}", registro):
        if registro in recuperadosDonantes:
            for provincia in registro[0]:
                if provincia == "1":
                    print(f"Usted es de San José, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "2":
                    print(f"Usted es de Alajuela, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "3":
                    print(f"Usted es de Cartago, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "4":
                    print(f"Usted es de Heredia, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "5":
                    print(f"Usted es de Guanacaste, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "6":
                   print(f"Usted es de Puntarenas, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "7":
                   print(f"Usted es de Limón, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "8":
                  print(f"Usted es nacionalizado o naturalizado, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
                elif provincia == "9":
                    print(f"Usted es de partida especial de nacimientos, está registrado en el tomo {registro[1:5]} y el asiento {registro[5:]}.")
        else:
            print("El donador no es un donante aún.")
    else:
        print("La cédula no cumple con el formato correcto.")
#3
def listarDonadores():
    """
    Función:
    Entrada:
    Salida:
    """
    
    return
#4
def donadoresTotales():
    """
    Función:
    Entrada:
    Salida:
    """
    return
#5
def donadoresNoTipicos():
    """
    Función:
    Entrada:
    Salida:
    """
    return