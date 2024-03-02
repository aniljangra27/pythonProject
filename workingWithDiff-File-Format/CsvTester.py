import pandas as pd

csvData = pd.read_csv('addresses.csv')

print(csvData)

# define Data Frame and assign column name
df = pd.DataFrame(data=csvData)
df.columns =['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']

# print formatted csv file
print(df)

# get specific column- column name should be same as csv column
print(df['Area Code'])

# get multiple column -
# Columns represent index - so to print multiple column keep the indexing same - like 'First Name', 'Last Name', 'Location ' ....
print(df[['First Name', 'Last Name']])
# print(df[['Location', 'State']]) # this will not work as index not correct

print('------------------------------')

# To select the first row
print(df.loc[0])

print('\nTo select the 0th,1st and 2nd row of First Name column only')
print(df.loc[[0,1,2], "First Name"])

print('\nTo select the 0th,1st and 2nd row of First and second column index only --use iloc ')
print(df.iloc[[0,1,2], [0,1]])