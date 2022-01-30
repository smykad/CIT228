
# prints a header
def print_header(myString, myNum):
    print(f"-----------------------------------------{myString} {myNum}-----------------------------------------")

def print_list(myString, myList):
    print(f"{myString}", end=": ")
    iteration = range(len(myList))
    limit = len(myList)
    for i in iteration:
        if i < limit-1:
            print(f"{myList[i]}", end=f", ")
        else:
           print(f"{myList[i]}")

def print_invites(myList, myString):
    iteration = range(len(myList))
    for i in iteration:
        print(f'{myList[i]}, {myString}')
        
def print_decline(myList, myString, mySub, myNewGuest, myNewString):
    print(f"{myList[mySub]}, {myString}")
    myList[mySub] = myNewGuest
    print_invites(myList, myNewString)

def modify_invite_list(guestOne, guestTwo, guestThree, myList, myString):
    myList.insert(0, guestOne)
    myList.insert(2, guestTwo)
    myList.append(guestThree)
    print('I found a bigger dinner table - woohoo')
    print(f'I am inviting {len(myList)} guests to dinner')
    print_invites(myList, myString)

def shrink_list(myList, myStringOne, myStringTwo, mySub):
    print("I am a flake - my dinner table won't be here in time and I can only " \
        "invite 2 people for dinner")
    index = 0
    iteration  = range(len(myList))
    for i in iteration:
        if index == mySub:
            break
        removed_guest = myList.pop()
        index += 1
        print(f'{removed_guest}, {myStringOne}')
    print_invites(myList, myStringTwo)
    
    iteration = range(len(myList))
    limit = len(myList)
    for i in iteration:
        if i < limit-1:
            print(f"Now removing {myList[i]} from guest list")
            del myList[i]
        else:
            print(f"Now removing {myList[0]} from guest list")
            del myList[0]
            print_list("Here's my revised guest list", myList)
    
    

# lists

myInvite = 'can you make it to dinner this Saturday?'
myDecline = 'cannot make it this Saturday'
myUninvite = 'I am sorry, I cannot have you over for dinner Saturday. Maybe next week?'
myGuestList = ['Douglas Adams', 'Grandpa', 'Urlica']

print_header('Exercise', '3-4')
print_invites(myGuestList, myInvite)

print_header('Exercise', '3-5')
print_decline(myGuestList, myDecline, 0, 'Dad', myInvite)

print_header('Exercise', '3-6')
modify_invite_list('John Cleese', 'Mark Hamil', 'Jeff Bridges', myGuestList, myInvite)

print_header('Exercise', '3-7')
shrink_list(myGuestList, myUninvite, myInvite, 4)