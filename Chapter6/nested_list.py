def header(myString):
    for element in myString:
        print("--", end="")
    print("\n", end="")

def nest(myDict):
    for key in myDict.keys():
        print(key)
        header(key)
        for subKey, value in myDict[key].items():
            print(f"{subKey}: ", end="")
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
        print("\n")

myNestedDict = {
    'dictA':{
        'key1':1,
        'key2':['1','2','5']
        },
    'dictB':{
        'key3':2,
        'key4':['3','4']
        },
    'dictC':{
        'key5':3,
        'key6':['5','6']
        }
}

nest(myNestedDict)