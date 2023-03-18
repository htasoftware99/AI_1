class Calculator:
    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2
        
    def multiply(self):
        return self.value1 * self.value2
    
    def division (self):
        return self.value1 / self.value2
    
print("Choose add(1), Choose multiply(2), Choose division(3)")
selection = input("select 1 or 2 or 3: ")
v1 = int(input("first value: "))
v2 = int(input("second value: "))
c1 = Calculator(v1, v2)
if selection == "1":
    add_result = c1.add()
    print("Add: {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply: {}".format(multiply_result))
elif selection == "3":
    division_result = c1.division()
    print("Division: {}".format(division_result))

    
# v1 = float(input("Enter a value: "))
# v2 = float(input("Enter a value: "))
# c1 = Calculator(v1, v2)
# add_result = c1.add()
# multiply_result = c1.multiply()
# print("Add: {}, Multiply: {}".format(add_result, multiply_result))
        