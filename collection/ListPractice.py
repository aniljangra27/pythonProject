# print function
def printfunction(listarr):
    print(listarr, "-- Length ", len(listarr))


# Insert and Append in list
studentList = [1, "anil", 500, 80.5]

printfunction(studentList)

# Insert
studentList.insert(10, "hello")  # higher index always append at last
studentList.insert(3, "hi")
printfunction(studentList)

# Append
studentList.append("How are you")
printfunction(studentList)

studentList.reverse()  # reverse list
printfunction(studentList)

# Single element list
stuList = ["Ram"]
print(type(stuList))

# List Comprehension - it is a way to compress ur code into one single line

nameList = ["Anil", "Ram", "Sham", "Jessica"]

print(".......... List Comprehension .............")
# create a new list using standard way
newNameList = []
for x in nameList:
    if "h" in x:
        newNameList.append(x)

print(newNameList)  # it print ['Sham']

# create a new list using List Comprehension way
newComprehensiveList_1 = [x for x in nameList]
print(newComprehensiveList_1)  # ['Anil', 'Ram', 'Sham', 'Jessica']

newComprehensiveList_2 = [x for x in nameList if "a" in x]
print(newComprehensiveList_2)  # ['Ram', 'Sham', 'Jessica']

newComprehensiveList_3 = [x for x in nameList if x != "Ram"]
print(newComprehensiveList_3)  # ['Anil', 'Sham', 'Jessica']

newComprehensiveList_4 = [x.upper() for x in nameList]
print(newComprehensiveList_4)

newComprehensiveList_5 = [x if x != "Sham" else "Aarav" for x in nameList]
print(newComprehensiveList_5)

newComprehensiveList_6 = [x for x in range(10)]
print(newComprehensiveList_6)

newComprehensiveList_7 = [x for x in range(0,20,5)]
print(newComprehensiveList_7)