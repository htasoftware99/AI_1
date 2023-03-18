import pandas as pd
dictionary = {"NAME":["Ali","Veli","Hasan","Mehmet","Ayşe","Fatma"],
              "AGE":[15,16,17,18,19,20],
              "SALARY":[100,200,300,400,500,600]}
dataframe1 = pd.DataFrame(dictionary)
print(dataframe1)
head = dataframe1.head(6)
print(head)
print("*****************************")
tail = dataframe1.tail(1)
print(tail)