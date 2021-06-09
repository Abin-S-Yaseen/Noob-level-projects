#Basic Calculator

num1 = float(input('Enter the first number: '))
optr = input('Enter the operator: ')
num2 = float(input('Enter the second number and press Enter key: '))
  

def add():
    return num1 + num2
def subtract():
    return num1 - num2
def multiply():
    return num1 * num2
def divide():
    return num1 / num2

if optr == "+":
    print("The answer is " + str(add()))
if optr == "-":
    print("The answer is " + str(subtract()))
if optr == "*":
    print("The answer is " + str(multiply()))
if optr == "/":
    print("The answer is " + str(divide()))
    

