import random
import os
filename='Chapter10/guests.txt'

if os.path.exists(filename):
    os.remove(filename)

with open(filename, 'w') as guestsFile:
    guest=input("Please enter your name (q to quit)? ")
    while guest.lower() != 'q':
        number = random.randint(1,3)
        match number:
            case 1:
                print(f'Good day {guest}')
            case 2:
                print(f'Cowabunga {guest}')
            case _:
                print(f'Astalavista {guest}')
        guest+='\n'
        guestsFile.write(guest)
        guest=input("Please enter your name (q to quit)? ")
        
with open(filename) as guestsFile:
    print("----------Guests file----------\n")
    for line in guestsFile:
        print(line.strip())
        
        