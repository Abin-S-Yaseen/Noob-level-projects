import random
import time

p = random.randrange(1,21)
q = random.randrange(1,11)
r = random.randrange(1,6)
s = random.randrange(1,16)

print("Guess a number between 1 and 10")
confirm1 = input("Press 'Y' to confirm ")
if confirm1.upper() == 'Y':
    confirm2 = input(f"Add {p} to the guessed number and press 'Y' to continue ")
    if confirm2.upper() == 'Y':
        confirm3 = input(f"Subtract {q} from the current number and press 'Y' to continue ")
        if confirm3.upper() == 'Y':
            confirm4 = input(f"Multiply the current number by {r} and press 'Y' to continue ")
            if confirm4.upper() == 'Y':
                confirm5 = input(f"Add {s} to the current number and press 'Y' to continue ")
                if confirm5.upper() == 'Y':
                    c = input("Enter the the current number that you got after the calculations : ")
                    if type(c) == int or float:
                        guessed_num = (int(c) - s)/r + q - p
                        print(f"The number that you guessed in the beginning was {int(guessed_num)} !!!")
                        time.sleep(5)
                    else:
                        print("INVALID SYNTAX")
