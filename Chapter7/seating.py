def isValidInt():
    isItInt = False
    while isItInt is False:
        ret = input()
        try:
            int(ret)
            isItInt = True
        except ValueError:
            print("Please enter a digit", end=": ")
    return ret

def seating():
    validInput = False
    print("Please submit how many guests you are seeking a table for: ", end="")
    num = isValidInt()
    while validInput is False:
        if int(num) < 0:
            print("Please enter a valid digit", end=": ")
            num = isValidInt()
        elif int(num) <= 8:
            print("We have table ready for you!")
            validInput = True
        else:
            print("You must wait for a table")
            validInput = True

seating()