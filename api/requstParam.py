import requests
url_get='http://httpbin.org/get'
payload = {"name":"Joseph","ID":"123"}

r = requests.get(url_get, payload)
print(r.url)
print("request body:", r.request.body)

# view the response as a text
print(r.text)
print(r.json())
print(r.json()['origin'])