# tuples are unchangeable and immutable

x = ("apple", "banana", "cherry")

print(x)  # => ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)  # => ("apple", "kiwi", "cherry")

print("\n--------------------------------")

thisTuple = ("apple", "banana", "cherry")

y = list(thisTuple)
y.append("orange")

thisTuple = tuple(y)
print(thisTuple)  # => ("apple", "banana", "cherry", "orange")

print("\n--------------------------------")
# é possível mesclar tuplas !

thisTuple = ("apple", "banana", "cherry")
y = ("orange",)

thisTuple += y

print(thisTuple)  # => ("apple", "banana", "cherry", "orange")

print("\n--------------------------------")
# use gambiara para excluir item de uma tupla
thisTuple = ("apple", "banana", "cherry")

y = list(thisTuple)
y.remove("apple")

thisTuple = tuple(y)

print("\n--------------------------------")

thisTuple = ("apple", "banana", "cherry")
del thisTuple
print(thisTuple)  # this will raise an error because the tuple no longer exists
