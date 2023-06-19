class Pessoa:
    def __init__(self, nome, idade):
        self._name = nome
        self._idade = idade
    
    def cumprimentar(self):
        print(f"Olá, meu nome é {self._name}!")

    @property
    def name(self):
        return self._name
    
    @property
    def idade(self):
        return self._idade

    @name.setter
    def name(self, value):
        self._name = value

    @idade.setter
    def idade(self, value):
        self._idade = value

    @name.deleter
    def name(self):
        del self._name
        
p1 = Pessoa("Jean", 20)

p1.cumprimentar()
print(f"Eu tenho {p1.idade} anos!")