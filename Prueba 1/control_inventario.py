#Recibimiento
print ("Control de inventario")
print ("Sea bienvenido")

#Solicitud de la cantidad de productos
Ingreso = int(input ("Ingrese la cantidad de productos que desea registrar: "))
Valor_total = 0

#Registrar información de cada producto
while Ingreso > 0: 
    Producto = input ("1. Nombre del producto: ")
    Precio = float(input ("2. Precio del producto: "))
    Cantidad = int(input ("3. Cantidad disponible: "))

    if  Precio <= 0:
        print ("ERROR: el precio no puede ser menor a 0")
    elif Cantidad <= 0:
        print ("ERROR: la cantidad no puede ser menos que 0")
    else:
        Valor_total += Precio * Cantidad
        Ingreso -= 1
print(f"El valor total del inventario es: {Valor_total}")

print (f"Nombre del producto: {Producto}")
print (f"Valor total: {Valor_total}")