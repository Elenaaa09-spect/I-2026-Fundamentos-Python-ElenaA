print ("Bienvenido a la aplicación de cálculo de IMC")
nombre = input ("Ingrese su nombre:")
apellidos = input ("Ingrese sus apellidos: ")
edad = int (input ("Ingrese su edad: "))
peso = float (input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clsificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print ("\n--- RESULTADOS ---")
print("Nombre:", nombre, apellidos)
print("edad:", edad)
print("IMC:", round(imc, 2))
print("Clasificación:", clasificacion)