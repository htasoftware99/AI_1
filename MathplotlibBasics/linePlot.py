import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("MathplotlibBasics\iris.csv")
df1 = df.drop(["Id"],axis=1)
print(df1)
# df1.plot()
# plt.show()
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa", linestyle = ":", alpha = 0.5)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor", linestyle = ":", alpha = 0.6)
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "purple", label = "virginica", linestyle = ":", alpha = 0.7)
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()