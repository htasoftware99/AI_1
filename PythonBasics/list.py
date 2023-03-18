_list=[1,2,3,4,5,6]
print(type(_list))
list_str=["Monday","Tuesday","Wednesday"]
print(type(list_str))

print(_list[5])
print(_list[-1]) #last value
print(_list[0:3]) #take 1,2,3 don't take others
print(_list[1:4]) # start from 1. index until 4.index except for others
print(_list[4:])
print(_list[:4])

#List methods
list_str.append("Thursday")
print(list_str)
list_str.remove("Thursday")
print(list_str)
list_str.reverse()
print(list_str)

list_2 = [5,6,8,1,3,5,1,9]
list_2.sort()
print(list_2)