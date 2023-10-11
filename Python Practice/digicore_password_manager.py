#welccome message to DigiCore clients
print("Welcome DigiCore Users!")
print("This is a password storage manager.\nPlease enter your information carefully.")


def new_credentials():
#getting user name and creating user name for clients
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    username = first_name[0].lower() + last_name.lower()    
    
    url_website = input("Enter the URL: ")
    while True:
            password = input("Enter your password: ")
            #using While True loop to validate the password 
            # if and elif checks if the password has met all the criteria
            if len(password) < 8:
                print("Your password is too short.\n")
            elif not any(char.isdigit() for char in password):
                print("Your password does not contain a number.\n")
            elif not any(char.isupper() for char in password):
                print("Your password does not contain a capital letter.\n")
            else:
                #else statement is used when the password has met all the criteria
                #break statement is used to exit the loop
                print("Your password is strong\n")
                break
            

    with open("saved_credentials.txt", "a") as file:
        file.write(f"Hello {first_name} {last_name}\n")
        file.write("These are your credentials: \n")
        file.write(f"The username is: {username}\n")
        file.write(f"The URL associated: {url_website}\n")
        file.write(f"The pasword is: {password}\n")
        
def view_saved_credentials():
    try:
        with open("saved_credentials.txt", "r") as file:
            saved_credentials = file.read()
            if saved_credentials:
                print("These are your saved credentials:\n")
                print(saved_credentials)
            else:
                print("You do not have any saved data.")
    except FileNotFoundError:
        print("No saved credentials found.")
        
choice = " "
while choice != "q":
    print("Please select from the following options") 
    print("\n[1] Enter 1 to add a new url entry.")
    print("\n[2] Enter 2 to view the saved credential.")
    print("\n[q] Enter q to exit.\n")    
    
    choice = input("\nMake your choice: ")
    
    if choice == "1":
        new_credentials()
    elif choice == "2":
        view_saved_credentials()
    elif choice == "q":
        print("Exising the program. Have a good day!")
        break   
    else:
        print("Invalid option, please try again.")
        
