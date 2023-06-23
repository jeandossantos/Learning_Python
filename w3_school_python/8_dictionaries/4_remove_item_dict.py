thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.pop("model")  # removendo o item model
print(thisDict)  # => {"brand": "Ford", "year":"1964"}

del thisDict["year"]  # removendo o item year
print(thisDict)  # => {"brand": "Ford"}
