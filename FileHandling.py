import os
file = open('testfile.txt', 'r')

# for eachLine in file:
#     print(eachLine)

print(file.read())
print(file.readline())
file.close()

with open('testfile.txt') as file1:
    print(file1.read())

print('.........................')
# create file
file3 = open('testfile2.txt','w');
file3.write("Testing..\n")
file3.write("Hi, There\n")
file3.write('How are you\n')
file3.close()

with open('testfile2.txt') as writeFile:
    print(writeFile.read())
print('.........................')

# Append file
file4 = open('testfile2.txt', 'a')
file4.write('All good, thanks!')
file4.close()
with open('testfile2.txt') as appFile:
    print(appFile.read())

# Remove file

# if os.path.exists('testfile.txt'):
#     os.remove('testfile.txt')
# else:
#     print("hello")