def basicTestFunciton():
    print("This is concat function in Python")


# Pass parameter to the function
def acceptParamFunction(x, y):
    print("Param passed", type(x), y)


# Call the function
basicTestFunciton()
acceptParamFunction("one", "two")
acceptParamFunction(1, 2)
acceptParamFunction(1.0, "test")

print("..............................")
# Pass function as a param and list
empNames = ["ram","sham","jessica","aarav"]
def printName(name):
    print("Emp name is ",name)

def employeeDetails(name, listEmpName):
    for i in empNames:
        name(i)

# call the function
employeeDetails(printName, empNames)