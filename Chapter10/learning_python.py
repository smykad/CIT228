#
#  Hands on #1
#


#
#  Try it yourself 10-1
#

filename = 'Chapter10/learning_python.txt'

with open(filename) as pythonFile:
    myFile = pythonFile.read()

#
#  10-1 I - Output from read()
#
print("----------Output from read()----------")
print(myFile)

#
#  10-1 II - Looping over the file
#

print("----------Output from for loop inside with...open----------")
with open(filename) as pythonFile:
    for line in pythonFile:
        print(line)
        
#
#  10-1 III - working with a list
#

print("----------Output from readlines()----------")

with open(filename) as pythonFile:
    myFile=pythonFile.readlines()
    
print("Original list=", myFile)

for line in myFile:
    print(line)


#
# 10-2 Try it yourself
#

print("----------Replacing Python with C#----------")

with open(filename) as pythonFile:
    for line in pythonFile:
        print("Original: ", line)
        print("Modified: ", line.replace("Python", "C#"))
