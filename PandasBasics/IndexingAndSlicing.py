import pandas as pd
dictionary = {"NAME":["Ali","Veli","Hasan","Mehmet","Ayşe","Fatma"],
              "AGE":[15,16,17,18,19,20],
              "SALARY":[100,200,300,400,500,600]}
dataframe1 = pd.DataFrame(dictionary)
#print(dataframe1)
print(dataframe1["NAME"])
print(dataframe1["AGE"])
#print(dataframe1.AGE)
dataframe1["New Feature"] = [-1,-2,-3,-4,-5,-6]
print(dataframe1["New Feature"])
print(dataframe1.loc[:, "AGE"])
print(dataframe1.loc[:3, "AGE"])
