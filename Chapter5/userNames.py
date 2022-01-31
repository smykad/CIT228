def compare_users(myString):
    
    myList = ['marvin', 'ford', 'arthur', 'zAyphod', 'slartibartfast']
    
    lowList = []
    for item in myList:
        lowList.append(item.lower())
    
    if myString.lower() in lowList:
        print(f'I\'m sorry the username {myString.title()} is already taken, please enter a new username!')
    else:
        lowList.append(myString)
        print(f'The username {myString} has been added')
        
def main():
    
    myList = ['fred', 'marVin','wilma', 'pebbles', 'zayPhod'] 
    
    lowList = []
    for item in myList:
        lowList.append(item.lower())
    
    iteration = range(len(lowList))
    
    for i in iteration:
        compare_users(lowList[i])

main()
