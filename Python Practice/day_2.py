# The list of lollies to print to the screen
lolly_list = [
    "Fantales", 
    "Snakes Alive", 
    "Minties", 
    "Liquorice Allsorts", 
    "Strawberries & Cream", 
    "Life Savers", 
    "Banana Lollies", 
    "Fruit Pastilles", 
    "Sherbies"
]

# The number of lollies the user will be allowed to choose
allowance = 5


# The list used to store all of the lollies selected inside of
lollies_cart = []

# Print all of the candies to the screen and their index in brackets
for lolly in lolly_list:
    print(f"{lolly_list.index(lolly)} : {lolly} ")

# Another option to run the for loop involves Python's enumerate method
# This method obtains both the index and the value of an item during a for loop
# for index, lolly in lolly_list:
#     print(index, lolly)
for selection in range(allowance):
    selection = int(input("Which lolly would you like to bring home?: "))
    lollies_cart.append(lolly_list[selection])
# Run through a loop which allows the user to choose which candies to take home with them

# Add the lolly at the index chosen to the lolly_cart list
# Loop through the lolly_cart to say what lollies were brought home
print("I brought home with me...")
for lollies in lollies_cart:
    print(lollies)
    
    