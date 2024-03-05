import json
# json.dump() method can be used for writing to JSON file.
# person = {
#     'first_name' : 'Mark',
#     'last_name' : 'abc',
#     'age' : 27,
#     'address': {
#         "streetAddress": "21 2nd Street",
#         "city": "New York",
#         "state": "NY",
#         "postalCode": "10021-3100"
#     }
# }

# Open json file
with open('samplejson.json') as jsonFile:
    fileContent = jsonFile.read()

print(fileContent)
# Parse Json file
with open('samplejson.json') as user_file:
    loadContent = json.load(user_file)

print(loadContent)

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('samplejson1.json', 'w') as file_w:
    json.dump(person_dict, file_w)

print(fileContent)