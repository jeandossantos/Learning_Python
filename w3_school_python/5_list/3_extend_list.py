thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
print(thislist)
print("################################")
# vocÊ pode extender tupla também

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
print(thislist)
