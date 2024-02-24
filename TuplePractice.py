# Tuple are similar like list - only difference is that Tuple are un-changeable
# Tuple are declared using () bracket
# There is no insert and append function in Tuple

studentTuple = (1, "Ram", 800, 56.9)
print(studentTuple)

# Tuple must have multiple values or even a comma - tuple do not have single value
# If single element is declared it treat as string/number/....
stuTuple = ("Hello")    # This will be considered as a String instead of Tuple
print(type(stuTuple))   # <class 'str'>

stu_Tuple = ("Hello",)
print(type(stu_Tuple))   # <class 'tuple'>


# How to add an element in Tuple
# - To add an element in Tuple fist it should be converted into list and then back to tuple

stu_list = list(studentTuple)
stu_list.insert(1, "shri")

print(tuple(stu_list))