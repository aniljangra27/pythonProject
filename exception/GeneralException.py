def calculation(num):
    try:
        result = num / (num - 2)
        print (f"Result: {result}")
    except Exception as e:
        print("An error occurred!!!")
# Test case
user_input = float(input("Enter a number: "))
calculation(user_input)