print ("Cajero automático")
print ("Bienvenido al cajero automático")
saldo = 159

while True:
    print ("1. Consultar saldo")
    print ("2. Retirar dinero")
    print ("3. Depositra dinero")
    print ("4. Salir")
    opcion = int (input("Seleccione una opción: "))

    if opcion == 1:
        print (f"Su saldo es: {saldo}")

    elif opcion == 2:
        cantidad = int (input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print ("No tiene suficiente saldo")
        else:
            saldo = saldo - cantidad
            print (f"Ha retirado: {cantidad}")

    elif opcion == 3:
        cantidad = int (input("Ingrese la cantidad que desea depositar: "))
        saldo = saldo + cantidad
        print (f"Ha depositado: {cantidad}")

    elif opcion == 4:
        print ("Gracias por usar el cajero automático")
        break

    else:
        print ("Opción no válida")