import numpy as np
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
array3 = np.vstack((array1,array2))
array4 = np.hstack((array1,array2))
print(array3)
print(array4)
