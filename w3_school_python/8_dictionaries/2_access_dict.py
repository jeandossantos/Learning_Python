thisDict = dict(name="Jean", surname="Santos", age=28)

# accessing the dictionary
print("My name is", thisDict["name"])
print("My surname is", thisDict.get("surname"))

print("\n################################")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# pegando as chaves do dict
x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

print("\n################################")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# pegando os valores do dict
x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change

print("\n################################")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change
print("\n################################")

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisDict dictionary")
