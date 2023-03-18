import pandas as pd
dictionary = {"NAME":["Ali","Veli","Hasan","Mehmet","Ayşe","Fatma"],
              "AGE":[15,16,17,18,19,20],
              "SALARY":[100,200,300,400,500,600]}
dataframe1 = pd.DataFrame(dictionary)
mean_value = dataframe1.SALARY.mean()
print(mean_value)

dataframe1["salary_status"] = ["low" if mean_value > salary else "high" for salary in dataframe1.SALARY]
for salary_status in dataframe1["salary_status"]:
    if salary_status == "high":
        print("low")
    else:
        print("high")
