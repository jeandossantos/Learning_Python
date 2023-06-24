def myFunction():
    print("Some function")


myFunction()
# quando você não sabe quantos argumentos vão ser passados para a função

print("\n################################")


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

print("\n################################")
# argumentos nomeados, dessa forma a ordem não importa


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")
print("\n################################")
# se o numero de keywords é desconhecidos... add **


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")
print("\n################################")
# valor padrão para argumento


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("\n################################")


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
