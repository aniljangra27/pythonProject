from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

# print(soup.prettify())

# read html tags
print(soup.title, soup.name, soup.head)

h3Tag = soup.findAll(name=['h3', 'p'])
print(h3Tag)

print(soup.find(id='boldest'))

print(soup.find('a', href=True))