x = "awesome"


def myFunc():
    x = "fantastic"
    print("Python is " + x)  # Python is fantastic


myFunc()

print("Python is " + x)  # Python is awesome

print("#################################\n")

# Declarando variável global dentro de func


def my_func_2():
    global y  # só existe depois de my_func_2 é chamada
    y = "this is the variable inside my_func_2"


my_func_2()
print(y)  # this is the variable inside my_func_2

print("#################################\n")

x = "awesome"

# Mudando variável global dentro de função


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

print("#################################\n")
x = "awesome"


def myfunc():
    global x
    x = "fantastic"  # muda o valor da variável x globa


myfunc()

print("Python is " + x)  # Python is fantastic
