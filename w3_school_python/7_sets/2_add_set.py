thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")

print(thisSet)
print("\n################################")
thisSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisSet.update(tropical)  # une os dois sets

print(thisSet)
print("\n################################")
# set aceita qualquer iterable

thisSet = {"apple", "banana", "cherry"}
myList = ["kiwi", "orange"]
myDict = {"nome": "Jean", "idade": 12}

thisSet.update(myList)
thisSet.update(myDict)

print(thisSet)
print("\n################################")
