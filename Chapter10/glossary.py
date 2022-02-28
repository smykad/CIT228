import json

def menu(myString):
    print(myString)
    print("1) Create file\n2) Read file\n3) Add to file \n4) Quit\n\nEnter choice here: ", end='')
    selection = isValidInt()
    
    match int(selection):
        case 1:
            create(myDict)
        case 2:
            read('Chapter10/glossary.json')
        case 3:
            append('Chapter10/glossary.json')
        case 4:
            print("Thank you for using this program")
        case _:
            menu("Please enter a valid menu option")


def create(object):
    print("You are about to create a new file, existing data will be overwritten!\n (q to quit, any key to continue)\nEnter choice here: ", end='')
    overwrite = input()
    myString = 'Please make a selection from the menu'
    match overwrite.lower():
        case 'q':
            menu(myString)
        case _:
            with open('Chapter10/glossary.json', 'w') as write_file:
                json.dump(object, write_file, indent=4, sort_keys=True)
                print('glossary.json has been created\n')
                continue_prompt()
                menu(myString)
                

def read(filename):
    try:
        with open(filename) as read_file:
            myGlossary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist and cannot be found.")
        continue_prompt()
        menu("\nPlease make a different menu selection")
    else:
        print_dict(myGlossary)
        continue_prompt()
        menu('\nPlease make a selection from the menu')

def file_name_formatter(filename, myFirstNum, mySecondNum):       
    myStr = filename
    size = len(myStr)
    modStr = myStr[myFirstNum:size-mySecondNum]
    return modStr

def append(filename):
    myItem = new_item()
    myFilename = file_name_formatter(filename, 10, 5)
    try: 
        with open (filename, 'r+') as add_file:
            glossaryDict = json.load(add_file)
            glossaryDict.update(myItem)
            add_file.seek(0)
            json.dump(glossaryDict, add_file, indent=4, sort_keys=True)
            print(f'Data has been added to \'{myFilename}.json\'')
            continue_prompt()
            menu('\nPlease make a selection from the menu')
            
    except FileNotFoundError:
        print("The file doesn't exist and cannot be found.")
        continue_prompt()
        menu("\nPlease make a different menu selection")
        
def continue_prompt():
    input('Press any key to continue')
    
def new_item():    
    key = get_key()
    value = get_value()
    ret={key:value}
    return ret  

def get_key():
    print('Enter a Python term:', end='')
    ret = input()
    ret = ret.title()
    return ret

def get_value():
    print('Describe the python term: ', end='')
    ret = input()
    return ret


def print_dict(myDict):
    for key, value in myDict.items():
        print(f'{key.title()}: {value}')

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
      
myDict = {
    "List":"A collection of items in a particular order",
    "Dictonary":"Python data type that stores key:value pairs",
    "Loop":"In Python a for loop is used for iterating over a sequence",
    "If":"In Python If statements are conditional statements",
    "Variable":"Python variables are created when you assign a value to it",
    "Iteration":"General term for taking each item of something one after another",
    "Operator":"In python, operators are special symbols that designate some sort of computation",
    "Data Type":"Classification of data items in Python",
    "Indentation":"In python, when you are grouping lines of code, you need to indent them",
    "Line Length":"In Python 80 characters per line is the standard, but not mandatory"
}

menu('Please make a selection from the menu')