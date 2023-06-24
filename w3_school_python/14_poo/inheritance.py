class Person:
    def __init__(this, firstname, lastname):
        this.firstname = firstname
        this.lastname = lastname
    
    def print_name(this):
        print(f"My name is {this.firstname}", this.lastname)
        
p1 = Person(firstname="John", lastname="Doe")
p1.print_name()

class Student(Person):
    pass

student1 = Student("Jean", "Santos")
student1.print_name()

print("\n################################")

class Person:
    def __init__(this, firstname, lastname):
        this.firstname = firstname
        this.lastname = lastname
    
    def print_name(this):
        print(f"My name is {this.firstname}", this.lastname)
        
# quando você cria um construtor na classe filha
# é necessário chamar o __init__ da classe Pai para herdar o construtor
class Student(Person):
   def __init__(self, firstname, lastname, graduation_year):
        #Person.__init__(self, firstname, lastname)
        super().__init__(firstname, lastname)
        self.graduation_year = graduation_year
        
   def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)

student1 = Student("Jean", "Santos", "2025")
student1.print_name()
student1.welcome()