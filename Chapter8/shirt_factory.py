def isValidChoice(choices, myString):
    isValidChoice = False
    while isValidChoice is False:
        ret = input().lower()
        if ret in choices:
            isValidChoice = True
        else:
            print(f"Please enter a valid choice: {myString}", end=": ") 
    return ret

def description(myShirt, myQuote):
    myQuotes = ["I love Python", "In a world where you can be anything, be kind" ]
    if myQuote == "a":
        myQuote = myQuotes[0]
    else:
        myQuote = myQuotes[1]    
    print(f"\nYour shirt size is {myShirt} with the message '{myQuote}' printed on the front")

def shirt():
    sizeChoice = ["small", "medium", "large"]
    quoteChoice = ["a", "b"]

    print("Choose a shirt size? ", end="")
    myShirt = isValidChoice(sizeChoice, "small, medium or large")
    print("\nAvailable quotes: \n\na) I love Python\nb) In a world where you can be anything, be kind\n\nChoose a quote", end=": ")
    myQuote = isValidChoice(quoteChoice, "a, b")
    
    
    description(myShirt, myQuote)

shirt()

