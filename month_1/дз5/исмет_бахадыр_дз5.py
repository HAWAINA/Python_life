def rectangle(width, height):
    print(width * height)

value1 = float(input("Enter the width: "))
value2 = float(input("Enter the height: "))

rectangle(value1,value2)

def avarege(val, lst):
    for i in range(0, val):
        el = int(input("Enter the number: "))
        lst.append(el)
    avg = sum(a) / n
    print("meen value:",round(avg, 2))

n = int(input(" Enter the number of numbers: "))
a = []

avarege(n, a)

def menu(**menus):
    return menus

menuOne = menu(breakfast="оромо", lunch="самсы", dinner="бананы")
menuTwo = menu(breakfast="маннаякаша", lunch="бешбармак", dinner="нан")
print(menuOne)
print(menuTwo)
