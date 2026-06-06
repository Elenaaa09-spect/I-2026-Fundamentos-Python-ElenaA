#Recibimiento
print ("Control de inventario")
print ("Sea bienvenido")

#Solicitar cantidad de productos
cantidad_productos = int(input("¿Cuántos productos desea registrar?: "))

#Variable para acumular eñ valor total de inventario
total_inventario = 0

#Ciclo para registrar productos
for i in range (cantidad_productos):
    print("\nProducto", i + 1)
    nombre = input ("Nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    total = precio * cantidad
    total_inventario += total

#Validar precio
while True:
    precio = float(input("Precio del producto: "))
    if precio > 0 :
        break
    else:
            print ("Error: el precio debe de ser mayor que 0")

#Validar cantidad
while True:
     cantidad = int(input("Cantidad disponible: "))
     if cantidad > 0:
          break
     else: print ("Error: la cantidad debe de ser mayor que 0")

#Calcular valor total del producto
valor_total = precio * cantidad

#Acumular al inventario
total_inventario += valor_total

#Mostrar resultados del producto
print ("\nResultado")
print ("Producto:", nombre)
print ("Valor total:", valor_total)

#Estadística final
print ("\n==== RESUMEN DEL INVENTARIO ====")
print ("Valor total general del inventario:", total_inventario)
