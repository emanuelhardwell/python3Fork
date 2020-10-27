#
#

# funciones sencillas
def saludo(nombre):
    print("Hello " + nombre)


saludo("hardwell")
saludo("Emanuel")


# funcion con parametro de reserva
def saludoPro(name="persona"):
    print("Hello " + name)


saludoPro("juan")
saludoPro()

# funcion ejemplo suma
def suma(numero1, numero2):
    return numero1 + numero2


print(suma(1, 2))


# funciones LAMDA
resta = lambda number1, number2: number1 - number2

print(resta(10, 2))
