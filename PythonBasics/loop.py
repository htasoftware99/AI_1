# for loop
for i in range(1,11):
    print(i)
for i in "Ankara Ist":
    print(i)
for i in "Ankara Ist".split():
    print(i)

list = [32,54,2,1,5,4,2,4,7,8,6,1,]
print(sum(list))

count = 0
for i in list:
    count = count + i
    print(count)

# while loop
i = 0
while(i<4):
    print(i)
    i = i+1

result = len(list)
each = 0
count = 0
while(each < result):
    count = count + list[each]
    each = each + 1
    print(each)