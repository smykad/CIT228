# Methods

# method to print a list with string formatting
def print_list(myString, myList):
    print(f"{myString}", end=": ")
    iteration = range(len(myList))
    limit = len(myList)
    for i in iteration:
        if i < limit-1:
            print(f"{myList[i]}", end=f", ")
        else:
           print(f"{myList[i]}")

# Lists

myGames = ['Rust', 'Raft', 'Runescape']

print_list("Original List: ", myGames)
myGames.append('Overwatch')
print_list("List after append", myGames)
myGames.insert(0, 'Starcraft')
print_list("List after insert", myGames)
del myGames[0]
print_list("List after del", myGames)
myGames.pop()
print_list("List after using pop()", myGames)
print("List with temporary sort: ", end="")
print(sorted(myGames))
myGames.reverse()
print_list("List sorted in reverse", myGames)
myGames.sort()
print_list("List sorted in alphabetical order", myGames)
# Methods

# method to print a list with string formatting
def print_list(myString, myList):
    print(f"{myString}", end=": ")
    iteration = range(len(myList))
    limit = len(myList)
    for i in iteration:
        if i < limit-1:
            print(f"{myList[i]}", end=f", ")
        else:
           print(f"{myList[i]}")



# Lists

myGames = ['Rust', 'Raft', 'Runescape']

print_list("Original List: ", myGames)
myGames.append('Overwatch')
print_list("List after append", myGames)
myGames.insert(0, 'Starcraft')
print_list("List after insert", myGames)
del myGames[0]
print_list("List after del", myGames)
myGames.pop()
print_list("List after using pop()", myGames)
print("List with temporary sort: ", end="")
print(sorted(myGames))
myGames.reverse()
print_list("List sorted in reverse", myGames)
myGames.sort()
print_list("List sorted in alphabetical order", myGames)
print(f'There are {len(myGames)} games in my list')