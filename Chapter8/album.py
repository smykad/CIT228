def header(myString):
    for element in myString:
        print("-", end="")
    print("\n", end="")

def make_album(myArtist, myAlbum, mySongs=None):
    ret = {
        'Album': myAlbum, 
        'Artist': myArtist
    }
    if mySongs:
        ret['Songs'] = mySongs
    return ret

def print_dictionary(myDict):
    for key, value in myDict.items():
        myString = f"{key}: {value}"
        print(myString)
    header(myString)
        
def yes_no():
    print("Would you like to enter another album?")
    print("yes or no", end=": ")
    ret = input()
    ret = ret.lower()
    if ret == 'y' or ret == 'yes':
        ret = True
    else:
        ret = False
    return ret

def album_loop():
    myBool = True
    while myBool != False:
        user_album()
        myBool = yes_no()
    print("Have a nice day!")
        
    

    
def user_album():
    myArtist = input("Enter Album name: ")
    myAlbum = input("Enter Artist name: ")
    userAlbum = make_album(myArtist.title(), myAlbum.title())
    print_dictionary(userAlbum)

albumA = make_album('Tool', 'Fear Inoculum')
albumB = make_album('Celldweller','The Imperial March')
albumC = make_album('Rammstein','Mutter', 11)

albumD = make_album('joe', 'shmoe', 18)

print_dictionary(albumA)
print_dictionary(albumB)
print_dictionary(albumC)

album_loop()

