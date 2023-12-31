#rock paper scissors game 

import random as random

choices = ['rock', 'paper', 'scissors']
while True: 
    pc_choice = random.choice(choices)
    user_choice = input("Please enter your choice, 'rock', 'paper' or 'scissors': ")
    if user_choice == 'rock' and pc_choice == 'paper':
        print("You lost!")
        break
    elif user_choice == 'scissors' and pc_choice == 'paper':
        print("You win!")
        break
    elif user_choice == 'paper' and pc_choice == 'scissors':
        print("You win!")
        break
    elif user_choice == pc_choice:
        print("It's a tie!")
        break