import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x) # converte uma json para dictionary

print(y['name'])

print("\n--------------------------------")

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x) # converte um dict para json

print(y) # => x in json format

print("\n--------------------------------")


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\n--------------------------------")

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))