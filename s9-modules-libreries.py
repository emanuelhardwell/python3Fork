#
#
# Exist three types of modules:  OWN,    THIRDY PARTY,   PYTHON MODULES

# forma 1 de importar (Se importan todos los metodos)
import datetime

print(datetime.date.today())

print(datetime.timedelta(minutes=80))


# forma 2 de importar (Se importan solo los metodos que necesitas)
from datetime import date, timedelta

print(date.today())
print(timedelta(minutes=80))

print("**********************************")

#importar mi modulo propio
import s10fmathmodulo
s10fmathmodulo.add(10,30)
s10fmathmodulo.substract(10,30)

#instalar modulos de python
# pip install "nombreDelModulo"