#
#  Hands on 3 Try it yourself 10-6 and 10-7
#

def isValidInt():
    isItInt = False
    while isItInt is False:
        ret = input()
        try:
            int(ret)
        except ValueError:
            print("Please enter a digit", end=": ")
        else:
            isItInt = True
    return ret
def addition():
    print('Enter first number: ', end='')
    numOne = isValidInt()
    print('Enter second number: ', end='')
    numTwo = isValidInt()
    mySum = int(numOne) + int(numTwo)
    print(f'The sum of {numOne} and {numTwo} is: {mySum}')
def prompt():
    ret= input("Would you like to add two more numbers? (q to quit)")
    return ret
def main():
    print('----------Simple Addition----------')
    addition()
    add = prompt()
    while add.lower() != 'q':
        addition()
        add = prompt()
        
main()