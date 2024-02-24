# using Try- except

def divideByZeroTest(x, y):
    global result
    try:
        result = x // y
        print("Answer is ", {result})
    except ZeroDivisionError:
        print("Error: Cannot divide by zero", {result})


divideByZeroTest(4, 2)

# divideByZeroTest(2,0)
