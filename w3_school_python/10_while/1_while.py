i = 1

while i < 6:
    print(i)
    i += 1

print("\n--------------------------------")
# podemos usar o break para parar o while quando certa condição é alcançada

i = 1

while i < 10:
    print("Valo de i é:", i)

    if i == 5:
        break

    i += 1

print("\n--------------------------------")

i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        print("Valor de i é:", i)

print("\n--------------------------------")

i = 1
while i < 10:
    print("Valo de i é:", i)
    i += 1
else:
    print("O loop while acabou de acabar!")
