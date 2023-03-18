# parent class
class Animal:
    def __init__(self):
        print("Animal is created")
    def toString(self):
        print("Animal")
    def walk(self):
        print("Animal walks")

# child class
class Monkey(Animal):
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("monkey is created")
    def toString(self):
        print("Monkey")
    def climb(self):
        print("Monkeys can climb")

# child class
class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    def toString(self):
        print("Bird")
    def fly(self):
        print("Birds can fly")

m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()

b1 = Bird()
b1.toString()
b1.walk()
b1.fly()

print("*************************************************************************************")

class Website:
    "parent"
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def loginInfo(self):
        print(self.name + " " + self.surname)

class Website1(Website):
    def __init__(self, name, surname, id):
        Website.__init__(self, name, surname)
        self.id = id
    def login(self):
        print(self.name + " " + self.surname + " " + self.id)

p1 = Website("name", "surname")
p2 = Website("name", "surname", "123")