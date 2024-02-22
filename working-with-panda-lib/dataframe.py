# A DataFrame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
import pandas as pd
#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(data=x)

#display the result df
print(df)
print(df.dtypes)
print("Retrieve name only \n", df[['Name']])

# Get multiple columns
mCol = df[['Salary','Name','ID']]
print(mCol)

print()

#Constructing DataFrame from a dictionary including Series:
seriesData = {'col1': [0, 1, 2, 3], 'col2': pd.Series([1, 2, 3], index=[1, 2, 3])}
print(pd.DataFrame(data=seriesData, index=[0, 1, 2, 3]))
