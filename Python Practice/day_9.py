print("This is a rock, paper, scissors game!\n")

import random as random

choice = ['rock', 'paper', 'scissors']

pc_choice = random.choice(choice)

user_choice = input("Please enter your choice, 'rock', 'paper' or 'scissors': ").lower()
while True:
    if user_choice == 'rock' and pc_choice == 'paper':
        return f'You lost!'        
    elif user_choice == 'scissors' and pc_choice == 'paper':
        print("You win!\n")
        break
    elif user_choice == 'paper' and pc_choice == 'scissors':
        print("You win!\n")
        break

    else user_choice == pc_choice:
        print("It is a tie!\n")
        break
        
