import random

def printNum(a_num, a_var):
    print("Number " + str(a_num) + " =", a_var)

def printDiv(var_one, var_two):
    print(var_one, "/", var_two, "=", var_one/var_two)
    
def printFloor(var_one, var_two):
    print(var_one, "//", var_two, "=", var_one//var_two)
    
def printModulus(var_one, var_two):
    print(var_one, "%", var_two, "=", var_one%var_two)
    
def printPlus(var_one, var_two):
    print(var_one, "+", var_two, "=", var_one+var_two)
    
def printMinus(var_one, var_two):
    print(var_one, "-", var_two, "=", var_one-var_two)

def printMult(var_one, var_two):
    print(var_one, "*", var_two, "=", var_one*var_two)
    
def bothNum():
    printNum(1, num1)
    printNum(2, num2)   
    
def numFun():
    bothNum()
    printDiv(num1, num2)
    printFloor(num1, num2)
    printModulus(num1, num2)
    printPlus(num1, num2)
    printMinus(num1, num2)
    printMult(num1, num2)

num1 = random.randrange(1,100)
num2 = random.randrange(1,100)

numFun()

NUM2 = 25
num2 = NUM2

numFun()
