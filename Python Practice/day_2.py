



# Initial variable to track game play

print("Play a game \n")
choice = ["yes", "no"]
user_choice = input("yes or no: ")

# While we are still playing..

while user_choice == "yes":
    
    # Ask the user how many numbers to loop through
    user_input = input("How many numbers?: ")
    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    
    for i in range(int(user_input)):
        print(i)    
        # Print each number in the range

user_choice = input("yes or no: ")

    # Once complete...



