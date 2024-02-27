# The Fruityvice API web service which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The web service is completely free to use and contribute to.
import pandas as pd
import requests
import json

data = requests.get("https://fruityvice.com/api/fruit/all")
result = json.loads(data.text)
print(result)

# convert our json data into pandas data frame.
df1 = pd.DataFrame(data=result)
# print(df1)

#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(result)
print(df2)

cherry = df2.loc[df2["name"] == 'Cherry']
var = (cherry.iloc[0]['family']), (cherry.iloc[0]['genus'])
print(var)

df3 = df1.drop(columns=["name", "family"], inplace=True)
print(df3)