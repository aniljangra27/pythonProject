a = 1001
b = 1200
if a < b:
    print('%(var1)s is less then %(var2)s.' % {'var1': a, "var2": b})
else:
    print('%(var1)s is grater then %(var2)s.' % {'var1': a, "var2": b})

# for loop

for i in range(10):
    print(i)

# list

print(list(range(10)))

print(list(range(1,12)))

print(list(range(5,20,5)))