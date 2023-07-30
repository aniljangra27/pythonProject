x = "Hello, Welcome to String class!"

# multiple line String
y = """Helllo
How 
are 
you
?"""
print(y)

z = '''Multiline
with
single 
quote'''

# String represents as an array in Python
print(x[0],"  ",x[5])

# loop in String
for i in x:
    print(i)

# Search value inside the given String
print("Welcome" in x)

# Slice a string
print(x[2:5])
print(x[-5:-2])
print(x[2:])
print(x[:8])

# Modify the string - upper/lower case,
print(x.upper())
print(x.lower())

# Strip -  remove white space
a = "heloo    "
print(a.strip())

# replace the string
print(x.replace("H", "Y", 1))

# split the string with comma
print(x.split(','))

# concat the string
c = "Shri"
d = "Ram"
print(c + d)