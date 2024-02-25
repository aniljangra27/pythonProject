import numpy as np
nparray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.__version__)
print(nparray[1:8])
print(type(nparray))
print(nparray.dtype)

# change array value
nparray[6] = 20
print(nparray)

c = np.array([1, 2, 3, 4, 5, 6, 7])
c[3:5] = 300, 400   # Set the fourth element and fifth element to 300 and 400
print(c)
# Find the size ,dimension and shape for the given array c
print(c.size)
print(c.shape)
print(c.ndim)

# Find the sum of maximum and minimum value in the given numpy array
c1 = np.array([-10, 201, 43, 94, 502])
max_val = c1.max()
print(max_val)

min_val = c1.min()
print(min_val)

print(max_val + min_val)

