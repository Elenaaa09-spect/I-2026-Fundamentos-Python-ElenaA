#Recibimiento
print ("Control de inventario")
print ("Sea bienvenido")

#Solicitar cantidad de productos
cantidad_productos = int(input("¿Cuántos productos desea registrar?: "))

#Variable para acumular el valor total de inventario
total_inventario = 0

#Ciclo para registrar productos
for i in range (cantidad_productos):

    print("\nProducto", i + 1)

    nombre = input ("Nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))

    if precio <= 0:
        print ("ERROR: el precio debe de ser mayor que 0")
    elif cantidad <= 0:
        print ("ERROR: la cantidad debe de ser mayor que 0")
    else:
        valor_total = precio * cantidad

        #Acumular el valor de todos los productos
        total_inventario += valor_total
        print ("Producto:", nombre)
        print ("Valor total:", valor_total)

#Mostar la suma total del inventario
print ("\nValor total del inventario:", total_inventario)