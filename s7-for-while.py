#
#

# for
fruits = [
    "banana",
    "apple",
    "orange",
    "grape",
    "pineapple",
    "watermelom",
    "mangoes",
    "papaya",
]

for fruit in fruits:
    print(fruit)
print("********************************")

# for with if
for fruit in fruits:
    print(fruit)
    if fruit == "pineapple":
        print("you find the pineapple --------->")
print("********************************")

# for with if and break
for fruit in fruits:
    print(fruit)
    if fruit == "pineapple":
        print("you find the pineapple --------->    break")
        break
print("********************************")

# for with if and continue
for fruit in fruits:
    print(fruit)
    if fruit == "pineapple":
        print("you find the pineapple --------->    continue")
        continue
print("********************************")

# for in range
for rango in range(0, 10):
    print(rango)
print("********************************")

# for in string
for letras in "hardwell":
    print(letras)
print("********************************")

# while ----------------------------------------------------------------

contador = 10

while contador < 20:
    print(contador)
    contador = contador + 1
