import pandas as pd
dictionary = {"NAME":["Ali","Veli","Hasan","Mehmet","Ayşe","Fatma"],
              "AGE":[15,16,17,18,19,20],
              "SALARY":[100,200,300,400,500,600]}
dataframe1 = pd.DataFrame(dictionary)
filtering_1 = dataframe1.SALARY >200
print(filtering_1)
filtered_data = dataframe1[filtering_1]
print(filtered_data)
filtering_2 = dataframe1.AGE < 18
filtering_2 = dataframe1.AGE < 18
print(dataframe1[filtering_1 & filtering_2])
