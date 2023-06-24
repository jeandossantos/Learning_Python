class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} {self.age}"

p1 = Person(name='Jean', age=28)
print(p1) # <__main__.Person object at 0x7fbf046cafd0>
print("Name:", p1.name, "Age:",p1.age)

print("\n################################")
# classe com __str__ implementado
class Person:
    def __init__(this, name, age):  
        this.name = name
        this.age = age
        
    def __str__(this):
        return f"{this.name} {this.age}"
    

p1 = Person(name='Jean', age=28)
print(p1) # # => Jean 28 porque o __str__ está implementado dessa forma