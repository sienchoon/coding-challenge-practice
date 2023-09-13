# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Aussie Beef", "Steak and Kidney", "Chicken", "Shepherd's", "Spinach and Feta", "Curry", "Lamb and Rosemary", "Steak and Mushroom", "Apple", "Lemon Meringue"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Aussie Beef, (2) Steak and Kidney, (3) Chicken, (4) Shepherd’s, " +
          "(5) Spinach and Feta, (6) Curry, (7) Lamb and Rosemary, (8) Steak and Mushroom, " +
          "(9) Apple, (10) Lemon Meringue")

    pie_choice = input("Which would you like (note: enter the number): ? ")

    # Add pie to the pie list note that it is just the index of the pies, not the name of pie
    pie_purchases.append(pie_choice)

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete
print("------------------------------------------------------------------------")
print("You purchased a total of " + str(len(pie_purchases)) + "pies.")
