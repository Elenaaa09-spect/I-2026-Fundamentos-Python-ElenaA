import pandas

# Cargar rl archivo CSV
datos = pandas.read_csv ("Clase 08/Estudiantes.csv")

print (datos.head())

print (datos [["nombre", "apellido"]].head())

print (datos.describe())

print (datos ["edad"].max())

print (datos ["edad"].min())

estudiantes_de_nota_alta = datos [datos ["nota"] > 85]
print (estudiantes_de_nota_alta)

media_por_genero = datos.groupby ("sexo") ["nota"].mean()
print (media_por_genero)
