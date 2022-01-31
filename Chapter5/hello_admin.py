from re import M


def print_header(myString):
    print(f'-------------- {myString} --------------')

def del_all_users(myList):
    i = 1
    while i < 6:
        print(f'Removing user {myList[0]}')
        del myList[0]
        i += 1       

def main():
    
    has_users=True
    myList = ['admin', 'zayphod', 'arthur', 'ford', 'marvin']
    
    print_header('Exercise 5-8 where list has users')
    
    while has_users!=False:
        if len(myList)==0:
            print('We need to get some users!')
            has_users=False
        else:
            for user in myList:
                if user == 'admin':
                    print(f'Welcome back {user.title()}, would you like a status report?')
                else:
                    print(f'Welcome back {user.title()}, thank you for logging in again!')    
            print_header('Exercise 5-9 where list is empty')
            del_all_users(myList)

main()
