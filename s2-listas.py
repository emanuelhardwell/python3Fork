#
# listas sencilla
nombres = ["emanuel", "hardwell", "tiesto", "martin", "hardwell"]

# lista con varios tipos
variedades = ["perez", 1, "aena", 234, [1, 2, 3, 4], "hola"]

# lista con TUPLAS
lista_tuplas = list((1, 2, 3, 4, 5, 6))


### practicas de metodos y funciones
print(nombres)
print(dir(nombres))

# agregar un elemento
nombres.append("jorge")
print(nombres)

# agregar mas de 2 elementos
nombres.extend(["fedelovo", "wereber"])
print(nombres)

# remover el ultimo elemento
nombres.pop()
print(nombres)

# remover un elemento en especifico
nombres.remove("emanuel")
print(nombres)

# contar cuantos datos son iguales
print(nombres.count("hardwell"))

# ordenar los datos de una lista
nombres.sort()
print(nombres)

# ordenar los datos de una lista al reves
nombres.sort(reverse=True)
print(nombres)

# insertar elemento
nombres.insert(1, "wirri mau")
print(nombres)

# busca el indice del elemento
print(nombres.index("jorge"))


# eliminar todos los elementos de una lista
nombres.clear()
print(nombres)