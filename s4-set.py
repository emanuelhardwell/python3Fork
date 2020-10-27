#
# los SETS se utilizan para elementos que no necesitemos que  tengan indice,
# y debemos buscar el elemento por su nombre

sets = {"oaxaca", "puebla", "tlaxiaco", "puerto escondido", "pochutla"}

print(sets)
print(dir(sets))

# agregar elemento
sets.add("Hardwell york")
print(sets)

# eliminar elemento
sets.pop()
print(sets)

# eliminar un elemento especifico
sets.remove("pochutla")
print(sets)

# verificar que esta un elemento
print("puebla" in sets)

# eliminar el sets
del sets