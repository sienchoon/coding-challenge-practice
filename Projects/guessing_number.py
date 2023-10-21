import random

#guessing number game

print("I am thinking of a number between 1 and 20")
print("Can you guess the number?")
n = random.randrange(1, 20)
guess = int(input("Enter a number: "))
attempt = 1

while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter a number: "))
        attempt += 1
    elif guess > n:
        print("Too high")
        guess = int(input("Enter a number: "))
        attempt += 1
    else:
        break

print("You got it!")
print(f"The number was {n} and it took you {str(attempt)} attempts!")