class Mascota:
    def __init__ (self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def mostrar_informacion (self):
        print ("Nombre: ", self.nombre)
        print ("Especie: ", self.especie)
        print ("Edad: ", self.edad)
        print ()

mascotas = []

cantidad = int(input("¿Cuántas mascotas hay para registrar? "))

for i in range (cantidad):
    print("\nMascota", i + 1)

    nombre = input ("Nombre: ")
    especie = input ("Especia: ")
    edad = int(input("Edad: "))
    
    mascota = Mascota (nombre, especie, edad)
    mascotas.append (mascota)

for i in range (len(mascotas)):
    print ("Mascota", i + 1)
    mascotas [i].mostrar_informacion ()