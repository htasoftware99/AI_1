import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("MathplotlibBasics\iris.csv")
df1 = df.drop(["Id"],axis=1)

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalLengthCm,setosa.PetalWidthCm, color="red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalLengthCm,setosa.PetalWidthCm, color="blue", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalLengthCm,setosa.PetalWidthCm, color="green", label = "virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()