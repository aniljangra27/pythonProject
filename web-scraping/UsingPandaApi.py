import pandas as ps
import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# data = requests.get(url).text

htmlRead = ps.read_html(url)
print(htmlRead)

print(htmlRead[0].get(2))