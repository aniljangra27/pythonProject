import requests
import os
url = "https://www.ibm.com/"
req = requests.get(url)
# get request URL
print(req.url)

print()
# get request status code
print(req.status_code)
# http response header - as a dictionary key: value pair
print(req.headers)
# get specific http response header value from the dictionary
print(req.headers['Last-Modified'])

# get request headers
print(req.request.headers)
# print request method and body - None -> for GET
print(req.request.method, req.request.body, req.request.url)

path = os.path.join(os.getcwd(), 'response-text.txt')
with open(path, 'wb') as file:
    file.write(req.content)