import requests
url_post='http://httpbin.org/post'
payload = {"name":"Joseph","ID":"123"}

print(" ------ Post request --------")
res = requests.post(url_post, data=payload)
print(res.url, res.request.headers)
print(res.request.body)
print(res.request.method)


# get request
print("\n ------ GET request --------")
r = requests.get(url_post, payload)
print(r.url)
print(r.request.body)
print(r.request.method)
