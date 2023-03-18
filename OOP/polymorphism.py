class Employee:
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee: ", result)

class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        result =  100 + 100 * raise_rate
        print("CENG: ", result)
    
class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print("EEE: ", result)

e1 = Employee()
ce = CompEng()
eee = EEE()

employee_list = [ce, eee, e1]
for employee in employee_list:
    employee.raisee()

print("**************************************************************")

from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):pass
    @abstractmethod
    def perimeter(self):pass

    def toString(self):pass

class Square(Shape):
    def __init__(self,edge):
        self.__edge = edge
    def area(self):
        result = self.__edge**2
        print("Square Area: ",result)
    def perimeter(self):
        result = self.__edge*4
        print("Square perimeter: ",result)

    #override and polymorphism
    def toString(self):
        print("Square Edge: ", self.__edge)

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        result = self.__radius **2 * math.pi
        print("Circle Area: ", result)
    
    def perimeter(self):
        result = 2* math.pi*self.__radius
        print("Circle Perimeter:", result)
    
    def toString(self):
        print("Circle radius: ", self.__radius)

c = Circle(5)
c.area()
c.perimeter()
c.toString()
print("-----------------------------------------------------------")
c = Square(4)
c.area()
c.perimeter()
c.toString()