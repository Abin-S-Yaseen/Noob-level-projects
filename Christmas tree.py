import time

space = " "
x = 20
y = 18
z = 16
for i in range(1,10,2):
    print(space*x+("*"*i))
    x -= 1
for i in range(5,16,2):
    print(space*y+("*"*i))
    y -= 1
for i in range(9,22,2):