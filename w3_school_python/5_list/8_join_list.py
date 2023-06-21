# concatenando duas listas
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)  # => ['a', 'b', 'c', 1, 2, 3]

print("################################")
# you can also do like this:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)  # => ['a', 'b', 'c', 1, 2, 3]
# or also like this:

print("################################")
# extend method can extend just one list by time
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)

print(list1)  # => ['a', 'b', 'c', 1, 2, 3]
