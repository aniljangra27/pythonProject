import requests
from bs4 import BeautifulSoup

url = requests.get("http://www.ibm.com")
data = url.text
# print(url.content)
soup = BeautifulSoup(data, 'html5lib')

for hrefLink in soup.findAll('a', href=True):
    print(hrefLink," -- ",hrefLink.getText('href'))

for imgSrc in soup.findAll('img'):
    print(imgSrc.get('src'))

print(soup.get_attribute_list('img'))