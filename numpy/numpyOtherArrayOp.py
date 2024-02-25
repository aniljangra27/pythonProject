import numpy as np

# numpy.array() – Creates array from given values.
# numpy.zeros() – Creates array of zeros.
# numpy.ones() – Creates array of ones.
# numpy.empty() – Creates an empty array.

# Create a 3D array with (2, 3, 4)
arrShape = (2, 3, 4)
arr = np.zeros(arrShape) # fill these with zero's
print(arr.shape)
print()
print(arr)
print()
arr1 = np.ones(arrShape)
print(arr1)

X=np.array([[1,0,1],[2,2,2]])
out=X[0,1:3]
print(out)