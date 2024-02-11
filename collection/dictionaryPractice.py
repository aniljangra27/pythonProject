# A dictionary consists of keys and values. It is helpful to compare a dictionary to a list. Instead of being indexed numerically like a list, dictionaries have keys. These keys are the keys that are used to access values within a dictionary.
# Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
dictionary = {}
dict1 = {"fName":"anil","lName":"Kumar","age":40}
# dict2 = {"fName":"Jessi","lName":"Jangra","age":6}

dictionary.update(dict1)

print(dictionary.keys())
print(dictionary.values())
print(len(dictionary))
print(dictionary["fName"])

