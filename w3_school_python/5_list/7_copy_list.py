thisList = ["apple", "banana", "cherry"]
list2 = thisList
# mesma referencia
print("Mesma lista" if list2 is thisList else "São listas diferentes")

print("################################")
# copiando os valores de uma lista para outra
oldList = ["apple", "banana", "cherry"]

newList = thisList.copy()
# são listas diferentes!
print("Mesma lista" if newList is oldList else "São listas diferentes")

newList2 = list(newList)

# Ainda são listas diferentes!
print("Mesma lista" if newList is newList2 else "São listas diferentes")
