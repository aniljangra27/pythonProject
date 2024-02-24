a = 9
# input value and divide
try:
    b = int(input("Enter number to divide  "))
    a = a/b
    print("a= ", a)
except ZeroDivisionError:
    print("Invalid operation")
except ValueError:
    print("Not a valid argument")
except:
    print("An error occurred")
finally:
    print("finally block")