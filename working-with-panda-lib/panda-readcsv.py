import pandas as pd


emp = pd.read_csv('student.csv')
print(emp.head(3))
print(emp["mark"].unique())