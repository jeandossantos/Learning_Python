# log way
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

print("--------------------------------")

# short way
# newList = [x for x in fruits if "a" in x]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []


[print(x) for x in fruits if "a" not in x]  # [kiwi, "cherry"]

# retorna o item se NÂO for "banana", se for retorna "orange"

newList = [x if x != "banana" else "orange" for x in fruits]

print(newList)
print("--------------------------------")
