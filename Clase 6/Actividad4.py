archivo = open("C:\Users\Personas Invitadas\Desktop\I-2026-Fundamentos-Python-ElenaA\Clase 6\Lectura_actividad4.txt", "w")
archivo.write("Registro de estudiantes\n")
archivo.close()

print ("Bienvendo al registro de estudiantes")

Estudiantes = int (input ("Ingrese la cantidad de estudiantes que desea registrar: "))
Total_de_estudiantes = 0

for i in range (Estudiantes):
    print ("\nEstudiante", i + 1)
    Nombre = input ("1. Ingrese el nombre del estudiante: ")
    Carné = int (input("2. Ingrese el carné del estudiante: "))
    Nota_final = float (input ("3. Ingrese la nota final del estudiante: "))

    if Carné <=0:
        print ("ERROR: el carné no puede ser menor a 0")
    elif Nota_final < 0 or Nota_final > 100:
        print ("ERROR: la nota final debe estar entre 0 y 100")
    else:
        Total_de_estudiantes += 1

print ("El total de estudiantes registrados es: ", Total_de_estudiantes)
