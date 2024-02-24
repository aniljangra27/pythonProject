import pandas as pd
studentData = {'ID':[0,1,2,3],'Student':['Anil','Samuel','Terry','Evan'],'Age':[27,24,22,32],'Country':['India','Canda','UK', 'USA'],'Course':['Python','DS','ML','WEB'], 'Marks':[100,72,89,76]}

stuDf = pd.DataFrame(data=studentData)

# loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. This method includes the last element of the range passed in it.
# Access the column using the name
print(stuDf.loc[0, 'Student'])

# iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it.
# Access the value on the first row and the third column
print(stuDf.iloc[0, 3])

# Access the value on the first row and the third column
print(stuDf.iloc[0,2])

print(stuDf.loc[2:3,'Student':'Country'])