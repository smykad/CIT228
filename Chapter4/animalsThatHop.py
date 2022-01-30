# methods

def print_list(myString, myList, myListTwo):
    iteration = range(len(myList))
    for i in iteration:
        print(f"{myList[i]}", end="\n")
    print(myString)
    for i in iteration:
        print(f'{myList[i]} {myListTwo[i]}', end='\n')

# Lists

myAnimals = ['Rabbit', 'Kangaroo', 'Klipspringer']
myAnimalsDescriptions = ['are found all over the world', 'are native to Australia', 'are found in South Africa']

# Strings

myStatement = '*********Animals that Hop*********'
print_list(myStatement, myAnimals, myAnimalsDescriptions)

