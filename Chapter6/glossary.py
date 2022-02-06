def print_dict(myDict):
    for key, value in myDict.items():
        print(f"{key.title()}: \n\t{value}")
        
myDict = {
    "List":"A collection of items in a particular order",
    "Dictonary":"Python data type that stores key:value pairs",
    "Loop":"In Python a for loop is used for iterating over a sequence",
    "If":"In Python If statements are conditional statements",
    "Variable":"Python variables are created when you assign a value to it",
    "Iteration":"General term for taking each item of something one after another",
    "Operator":"In python, operators are special symbols that designate some sort of computation",
    "Data Type":"Classification of data items in Python",
    "Indentation":"In python, when you are grouping lines of code, you need to indent them",
    "Line Length":"In Python 80 characters per line is the standard, but not mandatory"
}

print_dict(myDict)