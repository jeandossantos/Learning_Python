# Logando variáveis no terminal

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # Python is awesome

# logando números
print("#################################\n")
x = 5
y = 10
print(x + y)  # 15

# vai ter erro ao logar isso
print("#################################\n")
x = 5
y = "John"
try:
    print(x + y)
except:
    print("ERRO ao tentar concatenar/somar número com string")

# assim funciona embora
print("#################################\n")
x = 5
y = "John"
print(x, y)  # 5 John
