print ("Cajero automático")
print ("Bienvenido al cajero automático")

#Función para consultar saldo
def consultar_saldo(saldo):
    print (f"Su saldo actual es: ${saldo}")

#Función para retirar dinero
def retirar_dinero (saldo):
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    if cantidad > saldo:
        print ("No tiene suficiente saldo")
    else:
        saldo = saldo - cantidad
        print (f"Ha retirado: ${cantidad}")
    return saldo

#Función para depositar dinero
def depositar_dinero (saldo):
    cantidad = int(input("Ingrese la cantidad que desea depositar: "))
    saldo = saldo + cantidad
    print (f"Ha depositado: ${cantidad}")
    return saldo

#Programa principal
saldo = 159
while True:
    print ("\n1. Consultar saldo")
    print ("2. Retirar dinero")
    print ("3. Depositar dinero")
    print ("4. Salir")
    opcion = int(input("Seleccione una opción:"))

    if opcion == 1:
        consultar_saldo (saldo)
    elif opcion == 2:
        saldo = retirar_dinero (saldo)
    elif opcion == 3:
        saldo = depositar_dinero (saldo)
    elif opcion == 4:
        print ("Gracias por usar el cajero automático")
        break
    else:
        print ("Opción no válida")