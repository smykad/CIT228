
# prints a header
def print_header(myString, myNum):
    print(f"-----------------------------------------{myString} {myNum}-----------------------------------------")

def print_list_header(myString):
    print(myString)
    print('-----------------------------------------')
    
def print_list(myString, myList):
    print_list_header(myString)
    iteration = range(len(myList))
    for i in iteration:
        print(f"{myList[i]}", end="\n")

myFood = ['steak', 'brussel sprouts', 'chicken', 'cheese', 'bacon', 'brocolli']
myNumbers = [13, 42, 1337, 8, 86, 9]
myMovies = ['A new hope', 'Life of Brian', 'Monty Python and the Holy Grail']
myFavoriteCombo = ['steak', 'brussel sprouts', 42, 13, 'Life of Brian', 'Monty Python and the Holy Grail']



print_header('Chapter 4, ', 'Hands on 1')
print_list('Food List', myFood)

print_list('Number List', myNumbers)

print_list('Movie List', myMovies)

print_list('Combo List', myFavoriteCombo)