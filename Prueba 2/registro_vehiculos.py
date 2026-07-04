class Vehiculo:
    def __init__ (self, Placa, Marca, Año):
        self.placa = Placa
        self.marca = Marca
        self.año = Año
    def mostrar_informacion (self):
        print ("Placa: ", self.placa)
        print ("Marca: ", self.marca)
        print ("Año: ", self.año)
        print ()

vehiculos = []

cantidad = int(input("¿Cuántos vehículos desea registrar? "))

for i in range (cantidad):
    print("\nVehículo", i + 1)

    placa = input ("Placa: ")
    marca = input ("Marca: ")
    año = int(input("Año: "))
    
    vehiculo = Vehiculo (placa, marca, año)
    vehiculos.append (vehiculo)

for i in range (len(vehiculos)):
    print ("Vehículo", i + 1)
    vehiculos [i].mostrar_informacion ()