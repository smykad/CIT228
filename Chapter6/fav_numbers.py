def print_dict(myDict, myString):
    for key, value in myDict.items():
        print(f"{key.title()}, {myString.lower()}: {value}")
        
myDict = {
    "LISa":20,
    "Dan":22,
    "Danielle":7,
    "Dylan":11,
    "Leighton":13    
}

myString = "your favorite numBer Is"

print_dict(myDict, myString)