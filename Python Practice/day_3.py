# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Aussie Beef", "Steak and Kidney", "Chicken", "Shepherd's", "Spinach and Feta", "Curry", "Lamb and Rosemary", "Steak and Mushroom", "Apple", "Lemon Meringue"]


# YOUR CODE HERE

#create pie list with indexing number

for pies in pie_list: #loop through pie list, print index associating with the pies
    print(f"({pie_list.index(pies)}) : {pies}")


print("Enter the number of pie that you would like to order: ")


