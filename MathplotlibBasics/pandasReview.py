import pandas as pd
df = pd.read_csv("MathplotlibBasics\iris.csv")
print(df.columns)
print(df.Species.unique())
print(df.info())
print(df.describe())
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
print(setosa.describe())
print(versicolor.describe())