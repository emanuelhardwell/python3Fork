#
# las tuplas se usan para los elementos que no van a cambiar por ejemplo
# los meses del año, las temporadas, datos de tu domicilio
# ya que los datos de las tuplas no se pueden actualizar

meses = (
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
)
print(meses)
print(dir(meses))

# metodos que tienen las tuplas
print(meses[3])
print(meses.count("january"))

print(meses.index("october"))

print(len(meses))
