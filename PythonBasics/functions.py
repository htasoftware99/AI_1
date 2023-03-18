import math
def first_func(var1, var2):
    output = (((var1+var2)*50)/100)*var1/var2
    return output
print(first_func(20,50))

#default and flexible functions
def calculate_areaofCircle(r):
    output = int(2*3.14*r)
    return output
print(calculate_areaofCircle(2))

def calculate_areaofCircle(r):
    output = 2*math.pi*r
    return output
print(calculate_areaofCircle(2))

def calculate_areaofCircle(r, pi=3.14):
    output = 2*math.pi*r
    return output
print(calculate_areaofCircle(2))

def calculate(height, weight, *args):
    print("lenght of Args: ", len(args))
    output = (height+weight) * args[0]
    return output
print(calculate(70,50,10,80,79))

#Lambda Function
def calculate(x):
    output = x*x
    return output
print(calculate(5))

calculate2 = lambda x: x*x
print("Result of lambda function: ", calculate2(5))