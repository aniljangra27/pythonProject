# Dictionaries are unordered, changeable, do not allow duplicate
# Dictionaries are like Map in Java
# Dictionaries are <key>:<value> pair

studentDist = {
    "name": "Ram",
    "RollNo": 101,
    "Class": "Master",
    "Subject": ["Math", "Science", "Physic"]
}

print(studentDist)

print(studentDist["Class"])  # print class name
# OR
print(studentDist.get("name"))
print(studentDist.get("Subject"))  # print Subject list name

print(studentDist.values())  # print values only

print(studentDist.keys())

print(studentDist.pop("name"))  # delete name
