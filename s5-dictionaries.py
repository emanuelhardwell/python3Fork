#
# dictionaries
# Se utiliza cuando necesitamos crear objetos,
# es similar a los JSON

products = {
    "name": "laptop",
    "price": 12000.99,
    "marca": "huawei",
    "modelo": "pro 14",
    "year": 2019,
}

print(type(products))
print(products)
print(dir(products))
print("         ****************         **************")

# sacar las llaves de mi diccionario
print(products.keys())

# sacar los items de mi diccionario
print(products.items())

# eliminar un elemento de mi diccionario
products.pop("year")
print(products)

# agregar un elemneto a mi diccionario
products.update({"descount": 2000.78})
print(products)


# array con varios diccionarios
array_productos = [
    {
        "name": "laptop",
        "price": 12000.99,
        "marca": "huawei",
        "modelo": "pro 14",
        "year": 2019,
    },
    {
        "name": "PC",
        "price": 12000.99,
        "marca": "sony",
        "modelo": "pro 14",
        "year": 2019,
    },
]

print(array_productos)