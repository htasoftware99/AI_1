import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = array.ravel()
print(a)
array2 = a.reshape(3,3)
arrayT = array2.T
print(arrayT)
print(arrayT.shape)
array3 = np.array([[1,2],[3,4],[5,6]])
array3.resize((3,2))