def isValidInt():
    isItInt = False
    while isItInt is False:
        ret = input()
        try:
            int(ret)
            isItInt = True
        except ValueError:
            print("Please enter a digit", end="")
    return ret


def multOfTen():
    print("Please enter a number and I will tell you if it is a multipe of 10", end=": ")
    num = isValidInt()
    if int(num) % 10 == 0:
        print(f"{num} is a multiple of 10")
    else:
        print(f"{num} is not a multiple of 10")
        
multOfTen()