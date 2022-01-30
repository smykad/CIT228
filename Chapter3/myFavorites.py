# Chapter 3 hands on assignment no. 1
# Lists



# prints a header
def print_header(myString, myNum):
    print(f"-----------------------------------------{myString} {myNum}-----------------------------------------")

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

# created a method to only do every other value in the list to get the
# 2nd/4th/6th value in the list
           
def print_every_other(myString, myList):
    otherList = []
    for index in range(1, len(myList),2 ):
        otherList.append(myList[index])
    print_list(myString, otherList)
    
# lets you choose which element you pick out of the list using this method

def print_firsts(myString, myListOne, myListTwo, myListThree, i):
    print(f"{myString}", end=": ")
    print(f"{myListOne[i]}, {myListTwo[i]}, {myListThree[i]}, ")

# hands on one objectives 

def hands_on_one():
    print_header("Hands on", 1)
    print_list("Favorite foods", myFood)
    print_list(f"Lucky numbers", myNumbers)
    print_list("Favorite Movies", myMovies)
    print_list("Combo list", myFavoriteCombo)
    print_list("All movies", myMovies)
    print_every_other("2nd, 4th and 6th numbers", myNumbers)
    print_firsts("First food, first number and first movie", myFood, myNumbers, myMovies, 0)

def ins_sub(myString, myList, mySub, myIns):
    myList.insert(mySub, myIns)
    print_list(f"{myString}", myList)
    
def hands_on_two():
    print_header("Hands on", 2)
    myMovies.append("The big lebowski")
    print_list("Added movie", myMovies)
    ins_sub ("Added number at sub 3", myNumbers, 3, 72)
    ins_sub("Added food at sub 5", myFood, 5, "popcorn")

    del myFood[6]
    print_list("Deleted food [6]", myFood)

    myNumbers.pop()
    print_list("Deleted last number", myNumbers)

    myNumbers.pop(2)
    print_list("Deleted number at sub 2", myNumbers)
    
def hands_on_three():
    
    print_header("Hands on", 3)
    myMovies.sort()
    print_list("Sorted list", myMovies)
    print_list("Sorted list", myFood)
    print("Temp sorted list: ", end="")
    print(sorted(myNumbers))
    print_list("Unsorted list", myNumbers)
    myMovies.reverse()
    print_list("Sorted in reverse", myMovies)
    
def main():
    hands_on_one()
    hands_on_two()
    hands_on_three()
    
    
# Lists

myFood = ['steak', 'brussel sprouts', 'chicken', 'cheese', 'bacon', 'brocolli']
myNumbers = [13, 42, 1337, 8, 86, 9]
myMovies = ['A new hope', 'Life of Brian', 'Monty Python and the Holy Grail']
myFavoriteCombo = ['steak', 'brussel sprouts', 42, 13, 'Life of Brian', 'Monty Python and the Holy Grail']

# using the slice method you can get every other number 

# print(myNumbers[::2])

main()
=======
# Chapter 3 hands on assignment no. 1
# Lists



# prints a header
def print_header(myString, myNum):
    print(f"-----------------------------------------{myString} {myNum}-----------------------------------------")

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

# created a method to only do every other value in the list to get the
# 2nd/4th/6th value in the list
           
def print_every_other(myString, myList):
    otherList = []
    for index in range(1, len(myList),2 ):
        otherList.append(myList[index])
    print_list(myString, otherList)
    
# lets you choose which element you pick out of the list using this method

def print_firsts(myString, myListOne, myListTwo, myListThree, i):
    print(f"{myString}", end=": ")
    print(f"{myListOne[i]}, {myListTwo[i]}, {myListThree[i]}, ")

# hands on one objectives 

def hands_on_one():
    print_header("Hands on", 1)
    print_list("Favorite foods", myFood)
    print_list(f"Lucky numbers", myNumbers)
    print_list("Favorite Movies", myMovies)
    print_list("Combo list", myFavoriteCombo)
    print_list("All movies", myMovies)
    print_every_other("2nd, 4th and 6th numbers", myNumbers)
    print_firsts("First food, first number and first movie", myFood, myNumbers, myMovies, 0)

def ins_sub(myString, myList, mySub, myIns):
    myList.insert(mySub, myIns)
    print_list(f"{myString}", myList)
    
def hands_on_two():
    print_header("Hands on", 2)
    myMovies.append("The big lebowski")
    print_list("Added movie", myMovies)
    ins_sub ("Added number at sub 3", myNumbers, 3, 72)
    ins_sub("Added food at sub 5", myFood, 5, "popcorn")

    del myFood[6]
    print_list("Deleted food [6]", myFood)

    myNumbers.pop()
    print_list("Deleted last number", myNumbers)

    myNumbers.pop(2)
    print_list("Deleted number at sub 2", myNumbers)
    
def hands_on_three():
    
    print_header("Hands on", 3)
    myMovies.sort()
    print_list("Sorted list", myMovies)
    print_list("Sorted list", myFood)
    print("Temp sorted list: ", end="")
    print(sorted(myNumbers))
    print_list("Unsorted list", myNumbers)
    myMovies.reverse()
    print_list("Sorted in reverse", myMovies)
    
def main():
    hands_on_one()
    hands_on_two()
    hands_on_three()
    
    
# Lists

myFood = ['steak', 'brussel sprouts', 'chicken', 'cheese', 'bacon', 'brocolli']
myNumbers = [13, 42, 1337, 8, 86, 9]
myMovies = ['A new hope', 'Life of Brian', 'Monty Python and the Holy Grail']
myFavoriteCombo = ['steak', 'brussel sprouts', 42, 13, 'Life of Brian', 'Monty Python and the Holy Grail']

# using the slice method you can get every other number 

# print(myNumbers[::2])

main()
>>>>>>> db76f90efeb9bf5ab2e94cd69586922049d6acb8
