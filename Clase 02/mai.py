#Inicializar variables
nombre = "Elena"

#Solicitar al ususario su edad
edad:int = int(input("Cuál es tu edad?"))

#Calcular el año de nacimiento
anno_de_nacimiento = 2026 - 21

#Calcular mayoría de edad
print(anno_de_nacimiento)
mayor_de_edad = edad >= 18
print(mayor_de_edad)

#Finalización de variables a partir de diferentes datos
No_soy_yo = not (nombre == "Elena" and edad == 21)
Soy_yo = nombre == "Elena" and edad == 21
Quizás_soy_yo = nombre == "Elena" or edad == 21

#Imprimir variables en pantalla
print (No_soy_yo)
print (Soy_yo)
print(Quizás_soy_yo)

#Ejemplo de variables numéricas
x = 10
x += 5
print(x)