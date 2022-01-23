""" 
method for iterating through a dictionary to print it out
I'd need to make some modifications to this in order to
account for longer words like turqouise
"""

def print_dictionary_of_lists(a_dict):
    for key, value in a_dict.items():
        print(key, end="\t\t")
        iteration = range(len(value))
        limit = len(value)
        for i in iteration:
            if i < limit-1:
                print(f"{value[i]}", end=f"")
            else:
                print(f"{value[i]}")


#  Method for printing a header

def header(a_num):
    divider = "-------------------------------------------------"
    title = "Exercise"
    print(f"{divider}")
    print(f"\t\t{title} {a_num}")
    print(f"{divider}")
    
# Methods for upper and lower printing

def up(a_string):
    print(a_string.upper())

def low(a_string):
    print(a_string.lower())



header(1)

name="doug smyka"
print(name.title())
up(name)
low(name)
print("My first initial is: ", name[0].upper())

header(2)

noun = "tiger"
adj = "ferocious"
verb = "pounces"
ending = "on it's prey"
sentence1 = "the " + adj + " " + noun + " " + verb + " " + ending
sentence2 = f"the {adj} {noun} {verb} {ending}"


up(sentence1)
low(sentence2)

header(3)

# A common mistake that people make when trying to design something 
# completely foolproof is to underestimate the ingenuity of complete fools

stringVar1 = "\tA common mistake that people make" 
stringVar2 = "\twhen trying to design something"
stringVar3 = "\tcompletely foolproof is to"
stringVar4 = "\tunderestimate the ingenuity"
stringVar5 = "\tof complete fools"
stringVar6 = "\t\t-Douglas Adams"

print(f"One of my favorite quotes is: \n\n{stringVar1}\n{stringVar2}\n{stringVar3}\n{stringVar4}\n{stringVar5}\n\n{stringVar6}")


# I just wanted to use a dictionary instead of the way you had it set 
# up just go challenge myself since it's been a while since I coded in python

thisDict = {
  "Colors": "Food",
  "Orange": "Pizza",
  "Green": "Yogurt",
  "Purple": "Shrimp"
}

header(4)

print_dictionary_of_lists(thisDict)