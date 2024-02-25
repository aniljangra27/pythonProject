import numpy as np

a = np.array([5, 6, 7, 8])
b = np.array([1, 2, 3, 4])

c = np.add(a, b)

print(c)


# subtract array
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# Enter your code here
arr3 = np.subtract(arr1, arr2)
print(arr3)

# multiply array
print(np.multiply(arr1, arr2))

# divide
print(np.divide(arr1, arr2))

# ------------dot operation ------------

arr1 = np.array([3, 5])
arr2 = np.array([2, 4])
# dot operation: (x[0] * y[0]) + (x[1] * y[1])

print(np.dot(arr1, arr2))

# -------------Adding the constant 5 to each element in the array:-------
# Create a constant to numpy array
u = np.array([1, 2, 3, -1])
d = u + 5
print(d)

# -------- Line Space

lsp = np.linspace([2,3], num= 5)
print(lsp)
