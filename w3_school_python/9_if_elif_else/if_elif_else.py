a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


print("\n--------------------------------")
# se você só tem uma declaração, você pode colocar tudo em uma linha

if a > b:
    print("a is greater than b")

print("\n--------------------------------")
# if else em uma linha

print("A") if a > b else print("B")

print("\n--------------------------------")

a = 330
b = 330
# mostre A if a > b
# mostre = if a == b
# se não mostre B
print("A") if a > b else print("=") if a == b else print("B")
