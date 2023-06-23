# permite duplicados
thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thisTuple)

print("\n--------------------------------")

thisTuple = ("apple",)  # => adicione a virgula para ser tupla
print(type(thisTuple))

# NOT a tuple
thisTuple = ("apple")
print(type(thisTuple))  # => <class 'str'>

print("\n--------------------------------")
# Usando o construtor "tuple(("a", ", "c"))"
# note the double round-brackets
thisTuple = tuple(("apple", "banana", "cherry"))
print(thisTuple)  # => ("apple", "banana", "cherry")
