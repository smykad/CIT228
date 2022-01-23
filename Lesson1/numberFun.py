import random

def printNum(a_num, a_var):
    print("Number " + str(a_num) + " =", a_var)

def smoothOperator(var1, var2, operator):
    if operator == "/":
        num = var1/var2
    elif operator == "//":
        num = var1//var2
    elif operator == "+":
        num = var1+var2
    elif operator == "-":
        num = var1-var2
    elif operator == "*":
        num = var1*var2
    elif operator == "%":
        num = var1%var2
    print(var1, operator, var2, "=", num)
    
def bothNum():
    printNum(1, num1)
    printNum(2, num2)   
    
def numFunTwo():
    bothNum()
    smoothOperator(num1, num2, "/")
    smoothOperator(num1, num2, "//")
    smoothOperator(num1, num2, "%")
    smoothOperator(num1, num2, "+")
    smoothOperator(num1, num2, "-")
    smoothOperator(num1, num2, "*")

num1 = random.randrange(1,100)
num2 = random.randrange(1,100)

numFunTwo()

NUM2 = 25
num2 = NUM2

numFunTwo()