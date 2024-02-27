import requests
import os

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
print(os.getcwd())  # Current working directory

path = os.path.join(os.getcwd(), 'example1.txt')
r = requests.get(url)
with open(path, 'wb') as f:
    f.write(r.content)
