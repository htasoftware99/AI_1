import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("MathplotlibBasics\iris.csv")
df1 = df.drop(["Id"],axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.hist(setosa.PetalLengthCm, bins= 10)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()