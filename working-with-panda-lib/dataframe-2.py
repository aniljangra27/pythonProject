import pandas as pd

studentData = {'ID':[0,1,2,3],'Student':['Anil','Samuel','Terry','Evan'],'Age':[27,24,22,32],'Country':['India','Canda','UK', 'USA'],'Course':['Python','DS','ML','WEB'], 'Marks':[100,72,89,76]}

stuDf = pd.DataFrame(data=studentData)

print(stuDf)

# Retrieve the Marks column and assign it to a variable b
b = stuDf[['Marks']]
print(b)

# Retrieve the Country and Course columns and assign it to a variable c
c = stuDf[['Country', 'Course']]
print(c)

# To view the column as a series, just use one bracket
# Get the Student column as a series Object
x = stuDf['Student']
# print(type(x))
print(x)
