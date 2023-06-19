
class Animal:
    def __init__(self, nome):
        self._nome = nome

    def fazer_som(self):
        print(f"{self._nome} faz esse som!")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late!")

    def abanar_rabo(self):
        print("O cachorro está abanando o rabo!")

class Gato(Animal):
    pass


cachorro = Cachorro("Sadam")

cachorro.fazer_som()
cachorro.abanar_rabo()

mimi = Gato("Mimi")

mimi.fazer_som()