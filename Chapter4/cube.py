# kinda did it different than assignment but this should be fine

# prints a header
def print_header(myString, myNum):
    print(f"-----------------------------------------{myString} {myNum}-----------------------------------------")

def print_list(myString, myList, myListTwo):
    iteration = range(len(myList))
    index = 0
    for i in iteration:
        
        # checking what number it's on so that the list is uniform in print
        if index < 9:
            print(f' {myList[i]} {myString} {myListTwo[i]}', end='\n')
            index +=1
            
        # once it goes into two digits it no longer adds a space at the beginning
        else:
            print(f'{myList[i]} {myString} {myListTwo[i]}', end='\n')

def cube_list():
    # string variable for formatted print
    
    myString = 'cubed: '
    
    # create a list from 1 to 10
    numList = list(range(1, 11))
    
    # an empty list
    cubeList = []
    
    # populate the list with cubed values
    for i in numList:
        cubeList.append(i**3)
    
    print_header('Exercise', '4-8 and 4-9')
    # use the print list method to print the cubed values    
    print_list(myString, numList, cubeList)


cube_list()
