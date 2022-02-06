def print_dictionary(myDict):
    for key, value in myDict.items():
        print(f"The {key} river flows through", end=": ")
        if type(value)==list:
            iteration = range(len(value))
            limit = len(value)
            for i in iteration:
                if i < limit-1:
                    print(f"{value[i]}", end=f", ")
                else:
                    print(f"{value[i]}")
        else:
            print(value)
            
def header(myString):
    print(f"-------------------- {myString} --------------------")

def print_keys(myDict):
    for key, value in myDict.items():
        print(key)

def print_value(myDict):
    for key, value in myDict.items():
        if type(value)==list:
            iteration = range(len(value))
            limit = len(value)
            for i in iteration:
                if i < limit-1:
                    print(f"{value[i]}", end=f", ")
                else:
                    print(f"{value[i]}")
        else:
            print(value)

myDictOne = {
    "Danube":["Germany","Austria","Slovakia","Hungary","Coratia","Serbia","Romania","Bulgaria","Moldova","Ukraine"]
}

myDictTwo = {
    "Mississippi":"United States"
}

myDictThree = {
    "Amazon":["Brazil", "Bolivia", "Peru", "Ecuador", "Colombia", "Venezuela", "Guyana", "Suriname", "French Guiana"]
}

header("Rivers & Coutnries")
print_dictionary(myDictOne)
print_dictionary(myDictTwo)
print_dictionary(myDictThree)
header("Rivers")

print_keys(myDictOne)
print_keys(myDictTwo)
print_keys(myDictThree)

header("Countries")
print_value(myDictOne)
print_value(myDictTwo)
print_value(myDictThree)