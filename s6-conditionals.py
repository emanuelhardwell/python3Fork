#
#
# if sencillos ********************************
x = 6

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal than 5")
else:
    print("x is less than 5")


# if anidados ********************************
name = "emanue"
lastname = "vasque"
nickname = "hardwel"

if name == "emanuel":
    if lastname == "vasquez":
        if nickname == "hardwell":
            print("you are Emanuel vasquez Hardwell")
        else:
            print("you are not Emanuel Vasquez Hardwell")
    else:
        print("you are not Emanuel Vasquez")
else:
    print("You are not Emanuel")


# operadores logicos (and   or  not) ********************************
numero = 21
y = 4

if numero > 2 and numero <= 10:
    print("the number is greater than 2 and less or equal than 10")
if numero > 2 or numero <= 20:
    print("the number is greater than 2 and less or equal than 20")
if not (x == y):
    print("X is not equal than Y")
