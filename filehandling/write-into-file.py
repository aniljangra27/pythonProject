class RWFile:
    def __init__(self, fileText):
        self.fileText = fileText

    def writeIntoFile(self):
        with open('file1.txt', 'w') as file1:
            file1.write(self.fileText)

    def writeIntoFileFromList(self):
        # List of lines to write to the file
        Lines = ["Hallo, guten morgan\n", "Hallo, guten abend\n", "guten tag"]
        with open('file2.txt', 'w') as file2:
            for lines in Lines:
                file2.write(lines)

    # Append data in existing file
    def appendInExisting(self):
        appendLines =["\n0 in german ->", "null \n","1 -> ", "eins"]
        with open('file1.txt', 'a') as appendFile:
            for line in appendLines:
                appendFile.write(line)

    # Copying contents from one file to another
    def copyContent(self):
        # open source file
        with open('file-handling-imp-points', 'r') as sourceFile:
            # Open the destination file for writing
            with open('copycontect.txt', 'w') as destinationFile:
                # Read lines from the source file and copy them to the destination file
                for lines in sourceFile:
                    destinationFile.write(lines)



# create file object
rwFileObj1 = RWFile("Hi, there...")
rwFileObj1.writeIntoFile()

rwFileObj1.writeIntoFileFromList()
rwFileObj1.appendInExisting()

rwFileObj1.copyContent()
