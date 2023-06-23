# você pode concatenar tuplas
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  # => ("a", "b", "c", 1, 2, 4)

print("\n--------------------------------")
# multiplica o valor da tupla uma certa quantidade de vezes
fruits = ("apple", "banana", "cherry")
myTuple = fruits * 2

print(myTuple)  # => ("apple", "banana", "cherry", "apple", "banana", "cherry")
