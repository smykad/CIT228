def print_header(myString):
    print(f'*************** {myString} ***************')

def print_tuple(myTuple):
    for tup in myTuple:
        print(tup)

buffet=('eggs', 'ham', 'bread', 'cheese', 'apples')

# buffet[1]='bacon'

print_header('Buffet Menu')
print_tuple(buffet)

buffet=('eggs', 'bacon', 'bagel', 'cheese', 'apples')

print_header('New Buffet Menu')
print_tuple(buffet)
