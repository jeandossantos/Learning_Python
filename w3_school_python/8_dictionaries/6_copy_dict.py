thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# copiando o valor de um dict para outra variável NÃO a referência

thisDict2 = thisDict.copy()
thisDict3 = dict(thisDict)

# são diferentes dicts embora tenham os mesmos valores
print(thisDict is thisDict2)
print(thisDict is thisDict3)
