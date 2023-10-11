import os
#welccome message to DigiCore clients
print("Welcome DigiCore Users!")
print("This is a password storage manager.\nPlease enter your information carefully.")

#getting user name and creating user name for clients
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
username = first_name[0].lower() + last_name.lower()    
print(f"Hello {first_name} {last_name}")
print(f"This is your username: {username}")

#creating export file name and folder
file_output_name = f"{first_name}_{last_name}'s saved data.txt"
output_folder = "../Data"


#create several function that will make the program run
def add_url_website():
    url_website = input("Enter the URL associated with the saved credential: ")
    return f"The saved url is: {url_website}"

def password():
    saved_password = []
    print("Please create a password associated with this URL.\n")
    print("Your password should consist of atleast 8 characters, including a number and a capital letter.\n")
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
        saved_password.append(password)
    return saved_password

def export_data():
    
    
    file_path = os.path.join(output_folder, file_output_name)
    with open(file_path, "a", encoding="utf-8") as text:
        text.write(f"Hello {first_name} {last_name}\n")
        text.write("These are your credentials: \n")
        text.write(f"The username is: {username}\n")
        text.write(f"The URL associated: {add_url_website()}\n")
        text.write(f"The pasword is: {password()}\n")
    return f"Your data has been saved as {file_output_name}\n"
    
def view_saved_credentials():
    try:
        with open(file_output_name, "r", encoding="utf-8") as text:
            if text.read() == "":
                print("You do not have any saved data.")
            else:
                print(text.read())
    except FileNotFoundError:
        print("No saved credentials found.")


#this script runs the program
choice = " "
while choice != "q":
    print("Please select from the following options") 
    print("\n[1] Enter 1 to add a new url entry.")
    print("\n[2] Enter 2 to view the saved credential.")
    print("\n[q] Enter q to exit.\n")    
    
    choice = input("\nMake your choice: ")
    
    if choice == "1":
        add_url_website()
        password()
        export_data()
    elif choice == "2":
        view_saved_credentials()
    elif choice == "q:":
        print("Exising the program. Have a good day!")
        break   
    else:
        print("Invalid option, please try again.")

