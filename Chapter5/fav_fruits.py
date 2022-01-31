def if_else(myString):
    
    # list of my favorite fruit
    myList = ['mango', 'pineapple', 'grapefruit']
    
    # pass a string variable through and if else statement to test if it's in my favorite fruits
    
    # if it's in my list
    if myString in myList:
        print(f"It looks like you really like {myString}s")
    
    # if its not in my list
    else:
        print(f"It looks like {myString}s are not one of your favorite fruits")
        
# main method
    
def main():
    
    # generate a list to test in an if else loop
    
    myList = ['mango', 'orange', 'pineapple', 'papaya', 'grapefruit']
    
    # set up the range for the iteration 
    iteration = range(len(myList))
    
    # iterate through my list 
    for i in iteration:
        
        # pass the method to determine if it's a favorite fruit or not
        if_else(myList[i])


main()