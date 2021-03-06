import random

# in command prompt type pip install pyinputplus to use this module for python 

import pyinputplus as pyip

#   METHODS

#   ******************************
#   TAKE USER INPUT FOR MAX VALUE
#   ******************************


def max_value():
    ret = pyip.inputInt(min=1)
    return ret


#   ******************************
#   TAKE USER INPUT FOR NUMBER
#   OF QUESTIONS
#   ******************************

def num_of_questions():
    ret = pyip.inputInt(min=1)
    return ret


#   ******************************
#   RANDOMLY GENERATE QUESTIONS
#   ******************************
def question_generator(max_val):

    # Variables to increment

    guesses = 0
    global correct
    global incorrect

    #  Use max_value method to get range for values

    #  Assign values for question

    val1 = random.randint(0, max_val)
    val2 = random.randint(0, max_val)

    #  Print the question

    print(f"What is {val1} * {val2}? ")

    #  Set a boolean for the while Loop

    guessed = False

    while guessed is False:

        #  Take user input

        user_answer = pyip.inputInt()

        #  Increment guesses here

        guesses += 1

        #  If all guesses are exhausted

        if guesses == 3:
            print("You have exceeded your limit")
            print(f"{val1} * {val2} = {val1*val2}")

            #  Increment the counter 'incorrect'

            incorrect += 1
            guessed = True

        #  If user provides the correct answer

        elif user_answer == val1 * val2:
            print(f"That is correct! {val1} * {val2} is {user_answer}!")

            #  Increment the counter 'correct'

            correct += 1
            guessed = True

        #  If user provides incorrect answer
        else:
            print(f"Sorry try again!")
            continue


#   ******************************
#   MAIN METHOD
#   ******************************
def main():

    welcome_message()
    #  Prompt user for input

    print(f"Please enter a maximum value for the quiz: ", end='')
    max_val = max_value()

    #  Prompt user for input

    print(f"How many questions: ", end='')
    num = num_of_questions()
    for i in range(0, num):
        question_generator(max_val)

    #  Print results

    print(f"You got {correct} questions right and {incorrect} questions wrong")

    #  Print average

    print(f"Your grade is {(correct/num)*10}%")


#   ******************************
#   DISPLAY HEADER
#   ******************************
def welcome_message():
    print()
    print(f"\tMultiplication Quiz")
    print()

#   VARIABLES

correct = 0
incorrect = 0

#   MAIN

main()

#   EOF
