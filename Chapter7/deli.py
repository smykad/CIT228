sandwichOrders = ["Vegan", "Italian", "Steak", "Pastrami", "Greek", "Italian", "Pastrami", "Tuna", "Steak", "Pastrami"]

def print_list(myList):
    myList.reverse()
    iteration = range(len(myList))
    limit = len(myList)
    for i in iteration:
        if i < limit-1:
            print(f"{myList[i]}", end=", ")
        else:
            print(f"{myList[i]}")
    print("--------------------------------------------------")
    

def sammich(myList):
    finishedSandwiches = []
    while myList:
        mySammich = myList.pop()
        print(f"I made your {mySammich.title()} sandwich")
        finishedSandwiches.append(mySammich)
    print(f"\nSandwiches that were made today include: ")
    print_list(finishedSandwiches)
    noPastrami(finishedSandwiches)    

def noPastrami(myList):
    finishedSandwiches = []
    while myList:
        mySammich = myList.pop()
        print(f"You requested: {mySammich} sandwich")
        
        if mySammich == "Pastrami":
            print("Sorry we are out of pastrami!!")
        else:
            print(f"I made your {mySammich.title()} sandwich")
            finishedSandwiches.append(mySammich)
            
    print(f"\nSandwiches that were made today include: ")
    print_list(finishedSandwiches)

sammich(sandwichOrders)
    