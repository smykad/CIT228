def list_of_dict(myList):
    index = 0    
    while index < len(myList):
        for key, value in myList[index].items():
            print(f"{key}: ", end="")
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
        index += 1

myDictA ={
        'key1':1,
        'key2':['1','2','5']
}
myDictB = {
    'key3':2,
    'key4':['3','4']
}

myDictC = {
    'key5':3,
    'key6':['5','6']
}

listOfDict = [myDictA, myDictB, myDictC]

list_of_dict(listOfDict)
