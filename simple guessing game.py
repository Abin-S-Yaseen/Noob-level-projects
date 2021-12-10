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
