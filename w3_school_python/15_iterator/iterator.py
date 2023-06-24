mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("\n################################")
#criando uma class iteradora 

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1    
            return x
        else:
            raise StopIteration
    
numbers = MyNumbers()

n = iter(numbers)

print(next(n))
print(next(n))
print(next(n))

for x in n:
    print(x)