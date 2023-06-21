# declarando variáveis
x = int("5")
y = float("5")
z = str(5)

# verificando tipo
if type(x) == int:
    print("x is an integer")  # x is an integer

if type(y) == float:
    print("y is a float")  # y is a float

if type(z) == str:
    print("z is a string")  # z is a string
print("#################################\n")
# atribuindo em uma linha

x, y, z = "Orange", "Banana", "Cherry"

print(x)  # "Orange"
print(y)  # "Banana"
print(z)  # "Cherry"

# atribuindo um valor para várias variáveis
print("#################################\n")

x = y = z = "Orange"
print(x)  # "Orange"
print(y)  # "Orange"
print(z)  # "Orange"

print("#################################\n")
# unpacking (destructuring)

fruits = ["Orange", "Banana", "Cherry"]

x, y, z = fruits

print(x)  # "Orange"
print(y)  # "Banana"
print(z)  # "Cherry"

print("#################################\n")
