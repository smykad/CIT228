def print_header(myString):
    print(f"-----------------------{myString}-----------------------")

def print_list(myList):
    for i in myList:
        print(i)

def print_list_two(myString, myList):
    print(f"{myString}", end=": ")
    iteration = range(len(myList))
    limit = len(myList)
    for i in iteration:
        if i < limit-1:
            print(f"{myList[i]}", end=f", ")
        else:
           print(f"{myList[i]}")
    

def clone_list(myList):
    myNewList = myList[:]
    myNewList.append('cat')
    myNewList.append('dog')
    myNewList.append('llama')
    myNewList.append('mink')
    print_list(myNewList)
    myFirstThree = myNewList[:3]
    myMiddleThree = myNewList[3:6]
    myLastThree = myNewList[7:10]
    print_list_two('My first 3 animals are',myFirstThree)
    print_list_two('My middle 3 animals are', myMiddleThree)
    print_list_two('My last 3 animals are', myLastThree)


farmAnimals = ['horse', 'cow', 'pig', 'chicken', 'rooster', 'goat']

print_header('Original List')
print_list(farmAnimals)
print_header('New List')
clone_list(farmAnimals)