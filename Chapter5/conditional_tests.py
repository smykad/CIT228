def print_header(myString):
    print(f'=========== {myString} ===========')
    



def main():
    
    # variables
    
    headerOne = ' True Results'
    headerTwo = 'False Results'
    
    color = 'orange'
    food = 'pancakes'
    foodTwo ='Grits'
    num1 = 10
    num2 = 20
    breakfast = ['pancakes', 'waffles', 'eggs', 'bacon']   
    
    # header
    print_header(headerOne)
    
    print(f'{num1} <  {num2}: \t\t', num1<num2)
    print(f'{num1} <= {num2}: \t\t', num1<=num2)
    print(f'{color.title()} == {color.title()}: \t', color.title()==color.title())
    print(f'{color} == {color}: \t', color.lower()==color.lower())
    print(f'{food.title()} in breakfast?  ', food in breakfast)
    print(f'num1=={num1} and num2=={num2}? \t',  num1==10 and num2==20)
    print(f'num1=={num1} or num2!={num1}? \t',  num1==10 or num2!=10)
    
    # header
    print_header(headerTwo)
    
    print(f'{color} != {color}: \t', color!=color)
    print(f'{color.title()} == {color.upper()}: \t', color==color.upper())
    print(f'{num1} >  {num2}: \t\t', num1>num2)
    print(f'{num1} >= {num2}: \t\t', num1>=num2)
    print(f'{foodTwo} in breakfast? \t', foodTwo in breakfast)
    
main()