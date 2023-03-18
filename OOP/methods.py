class Square(object):
    edge = 5 
    def area(self):
        self.area = self.edge * self.edge
        print("Area: ", self.area)
square_1 = Square()
print(square_1.edge)
print(square_1.area())
# square_1.edge = 7
# square_1.area()

# Methods vs Functions
class Employee:
    age = 25
    salary = 1000
    def ageSalaryRatio(self):
        print("method: ", self.age / self.salary)

def ageSalaryRatio(age, salary):
    print("function: ", age / salary)

employee1 = Employee()
employee1.ageSalaryRatio()

ageSalaryRatio(30,3000)