class FileHandling:
    def readFile(self):
        # Step-1 open file in read mode
        with open('../testfile.txt','r') as file:
            file_stuff = file.read()
            print(file.name)
            print(file_stuff)

    def readFileLines(self):
        # read file line
        with open('../testfile.txt', 'r') as file:
            return file.readline() + file.readline()

    def saveFileToList(self):
        with open('../testfile.txt', 'r') as file1:
            fileList = file1.readline()
            return fileList

# Create object and access methods
fileHandlingObj = FileHandling()
fileHandlingObj.readFile()

firstLine = fileHandlingObj.readFileLines()
print("=----",firstLine)
print("===============================")
file_list = fileHandlingObj.saveFileToList()
print(file_list[0])