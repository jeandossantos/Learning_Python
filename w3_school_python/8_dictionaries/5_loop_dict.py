thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for i in thisDict:  # percorre as chaves
    print(i)  # mostra somente as chaves

print("\n--------------------------------")

for i in thisDict:
    print(thisDict[i])  # mostra o valor com a chave atual do loop

print("\n--------------------------------")

for x in thisDict.keys():  # percorre as chaves
    print(x)
print("\n--------------------------------")

for x, y in thisDict.items():
    print(x, y)
