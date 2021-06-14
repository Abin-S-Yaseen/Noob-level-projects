#Basic Calculator

while True:
    print('BASIC CALCULATOR')
    print('-----------------')
    num1 = float(input('Enter the first number: '))
    optr = input('Enter the operator: ')
    num2 = float(input('Enter the second number: '))
    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y

    if optr == "+":
        print(f"{num1} + {num2} = {add(num1,num2)}")
        input('Press ENTER Key to run again: ')
    if optr == "-":
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
        input('Press ENTER Key to run again: ')
    if optr == "*":
        print(f"{num1} * {num2} = {multiply(num1,num2)}")
        input('Press ENTER Key to run again: ')
    if optr == "/":
        print(f"{num1} / {num2} = {divide(num1,num2)}")
        input('Press ENTER Key to run again: ')
