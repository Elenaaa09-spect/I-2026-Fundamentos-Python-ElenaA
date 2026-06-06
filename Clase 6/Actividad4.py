archivo = open("Clase 6\Lectura_actividad4.txt", "w")
archivo.write("Registro de estudiantes\n")

print ("Bienvenido al registro de estudiantes")

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
        archivo.write(f"Nombre: {Nombre}, Carné: {Carné}, Nota final: {Nota_final}\n")
        Total_de_estudiantes += 1

archivo.close()

print ("El total de estudiantes registrados es: ", Total_de_estudiantes)
