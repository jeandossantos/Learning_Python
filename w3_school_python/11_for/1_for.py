# percorrendo uma lista
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

print("\n--------------------------------")
# percorrendo uma string

for x in "banana":
    print(x)
print("\n--------------------------------")
# usando o break
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break

print("\n--------------------------------")
# usando o continue
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue

    print(x)

print("\n--------------------------------")
# loop de 0 para 5 com range!
for x in range(6):
    print(x)

print("\n--------------------------------")

# arg 1 = começa o loop de 0
# arg 2 = percorre até o numero 30
# arg 3 = de 3 em 3
for x in range(0, 30, 3):  # vai parar no 29!
    print(x)

print("\n--------------------------------")
# podemos usar o else com o for também!
for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("\n--------------------------------")
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
