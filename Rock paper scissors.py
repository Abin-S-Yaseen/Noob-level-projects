import random

print('Basic Rules: ')
print('--------------------------------------')
print('1. Rock vs Paper => Paper wins')
print('2. Rock vs Scissors => Rock wins')
print('3. Paper vs Scissors => Scissors win')
print('--------------------------------------')
print("Press 'R' for Rock")
print("Press 'P' for Paper")
print("Press 'S' for Scissors")
print('-----------------------')

user_choice = input('Enter your choice here: ')

state = True
while state == True:
    if user_choice == 'R' or user_choice == 'r':
        print('You chose Rock!!!')
        state = False
    elif user_choice == 'P' or user_choice == 'p':
        print('You chose Paper!!!')
        state = False
    elif user_choice == 'S' or user_choice == 's':
        print('You chose Scissors!!!')
        state = False
    else:
        user_choice = input('Enter a valid input: ')
        state = True

comp_choice = random.randint(0,3)
