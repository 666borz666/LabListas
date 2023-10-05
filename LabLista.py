import re
def agregarDonadores(paciente):
    cedula=set()
    while len(cedula)< paciente:
        registro=input("Ingrese una cedula(9 digitos numericos: ")
        if re.match(r'^\d{9}$', registro):
            if registro in cedula:
                print("¡La cedula ya esta registradad!")
            else:
                cedula.add(registro)
                print(f"Cedula{registro} registrada correctamente. ")
        else:
             print("La cédula no cumple con el formato correcto. Inténtelo de nuevo.")
   
    print("Donantes registrados satisfactoriamente.")
     
def decodificarDonador(cedula):
      if cedula in registro:
          print("Donador registrado en Clorito Picado")
      else:
          print("Usted es de San José, está registrado en el tomo 5432, y el asiento 8765")
registro = input("Indique el número de cédula a decodificar: ")
if re.match(r'^\d{9}$', registro):
    decodificarDonador(registro)
else:
    print("La cédula no cumple con el formato correcto.")
    
