import pandas as pd
import numpy as np

#creating a dataframe
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

# add 10 to each element in a dataframe:
# applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

#  use DataFrame.transform() function to find the square root to each element of the dataframe
result = df.transform(func = ['sqrt'])
print(result)