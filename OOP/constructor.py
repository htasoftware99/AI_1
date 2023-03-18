class Animal:
    def __init__(self,a,b): # (name, age) = ("dog", 2) = (a,b)
        self.name = a
        self.age = b

    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    
a1 = Animal("dog", 2)
print(a1.age,a1.name)
a2 = Animal("cat", 4)
print(a2.age, a2.name)
a3 = Animal("bird", 6)
print(a3.age, a3.name)