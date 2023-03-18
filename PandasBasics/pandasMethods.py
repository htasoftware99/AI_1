import pandas as pd
dictionary = {"NAME":["Ali","Veli","Hasan","Mehmet","Ayşe","Fatma"],
              "AGE":[15,16,17,18,19,20],
              "SALARY":[100,200,300,400,500,600]}
dataframe1 = pd.DataFrame(dictionary)
#print(dataframe1)
print(dataframe1.columns)
print(dataframe1.info())
print(dataframe1.dtypes)
print(dataframe1.describe()) #numeric feature = columns(age, salary)