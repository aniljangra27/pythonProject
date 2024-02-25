import numpy as np
dimArray = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[8, 9, 10, 11],
                           [12, 13, 14, 15]],

                          [[16 ,17 ,27, 37],
                           [48, 58, 68, 78]]])

# array dimension - this is 3 dimension array like dimArray [3][2][4]
# here 3-> 2D arrays with 2 rows and 4 columns
#   Index=>0        Index=>1        Index=>2
#   [0, 1, 2, 3]    [0, 1, 2, 3]    [0 ,1 ,2, 3]
#   [4, 5, 6, 7]    [4, 5, 6, 7]    [4, 5, 6, 7]
print("Array dimension- ", dimArray.ndim)
# here dimArray[1][1][3] -> [1] -> second(Index=>1) 2D array, [1] -> 2nd row in that 2D array, [3] -> 3rd index element => ans: 15
secondArrayIndexElement = dimArray[1][1][3]
print(secondArrayIndexElement)

# here dimArray[2][1][3] -> [2] -> Third(Index=>2) 2D array, [1] -> 2nd row in that 2D array, [3] -> 3rd index element => ans: 78
thirdArrayIndexElement = dimArray[2][1][3]
print(thirdArrayIndexElement)

# here dimArray[0][0][2] -> [0] -> Third(Index=>0) 2D array, [0] -> 1st row in that 2D array, [2] -> 2nd index element => ans: 2
firstArrayIndexElement = dimArray[0][0][2]
print(firstArrayIndexElement)

