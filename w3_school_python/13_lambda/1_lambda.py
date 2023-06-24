# a lambda function
x = lambda a : a + 10
print(x(5))

print("\n----------------------------------------------------------------")
# pode receber vários argumentos
x = lambda a, b : a * b
print(x(5, 6))
print("\n----------------------------------------------------------------")
# pode ser usada para ser retornada em por uma função
def myFunc(x):
    return lambda a: a * x

myDoubler = myFunc(2)
print(myDoubler(3))

myTriple = myFunc(3)
print(myTriple(3))