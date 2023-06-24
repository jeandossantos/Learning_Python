# import my_module
import my_module as mx
from my_module import person1

#build-in module
import platform

mx.greeting("Jean")
print("\n--------------------------------")
a = person1["age"]

print(a)
print("\n--------------------------------")
print(platform.system())
print("\n--------------------------------")
print(dir(platform))