from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/IBM"

# get page using http request
httpResponse = requests.get(url)

# read the response and store in a variable
htmlContent = httpResponse.text

# print the content
# print(htmlContent)
print(htmlContent[:500]) # print first 500 char

# parse the content (response)
soup = BeautifulSoup(htmlContent, 'html.parser')

# find all anchor tag
for link in soup.findAll('a'):
    print(link)

print('\n*************************************\n')

# find all img src
for imgSrc in soup.findAll('img'):
    print(imgSrc['src'])