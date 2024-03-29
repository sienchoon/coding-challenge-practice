import os

print("This is a password storage manager.\nPlease enter your information carefully.")

first_name = input("Please enter your first name: ")
f_name = first_name.title()
last_name = input("Please enter your last name: ")
l_name = last_name.title()
username = first_name[0].lower() + last_name.lower()
saved_password = []
choice = ''
url_list = []
while choice != 'q':  
    print("\n[1] Enter 1 to create a new login entry.")
    print("[2] Enter 2 to add a new saved credential entry.")
    print("[q] Enter q to exit.")
    choice = input("\nMake your choice: ")
    if choice == '1':
        print("\nCreating a new login entry.")
        print("Your username has been created for you\n")
        print(f"Your username is: {username}\n")
        url_website = input("Enter the URL associated with the saved credential: ")
        url_list.append(url_website)
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
    elif choice == '2':
        print("Adding a new entry.\n")
        choice = ''
        while choice != 'q':  
            print("[1] Enter 1 to add a new URL entry.")
            print("[q] Enter q to exit.")
            choice = input("\nMake your choice: ")  
            if choice == '1':
                url_website = input("Enter the URL associated with the saved credential: ")
                url_list.append(url_website)
                print("Do you want to use the same password?")
                print("[1] Enter 1 to reuse the same password.")
                print("[2] Enter 2 to change the password.")
                choice = input("\nMake your choice: ")
                choice = ''
                if choice == '1':
                    if password == None:
                        print("You do not have a saved password, please enter a password.")
                        password = input("Enter your password: ")
                        if len(password) < 8:
                            print("Your password is too short.\n")
                        elif not any(char.isdigit() for char in password):
                            print("Your password does not contain a number.\n")
                        elif not any(char.isupper() for char in password):
                            print("Your password does not contain a capital letter.\n")
                        else:
                            print("Your password is strong\n")
                            break
                    else:
                        password = password
                        print("You reused the previous password.\n")
                        break
                    saved_password.append(password)
                elif choice == '2':
                    while True:
                        print("Please ensure the password contains atleast 8 charaters, including a number and a capital letter.\n")
                        password = input("Enter your password: ")
                        if len(password) < 8:
                            print("Your password is too short.\n")
                        elif not any(char.isdigit() for char in password):
                            print("Your password does not contain a number.\n")
                        elif not any(char.isupper() for char in password):
                            print("Your password does not contain a capital letter.\n")
                        else:
                            print("Your password is strong\n")
                            break
                        saved_password.append(password)  
                elif choice == 'q':
                    print("Exiting the program.\n")
                    break 
    elif choice == 'q':
        print("\nExiting the program. Have a good day!")
        break
    else:
        print("\nInvalid option, please try again.")

 #exporting the saved data to a text file in a different location       
file_output_name = f"{f_name}_{l_name}'s saved data.txt"
output_folder = "../Data"
file_path = os.path.join(output_folder, file_output_name)

with open(file_path, "a", encoding="utf-8") as text:
    text.write(f"Hello {f_name} {l_name}\n")
    text.write("These are your credentials: \n")
    text.write(f"The username is: {username}\n")
    text.write(f"The URL associated: {url_list}\n")
    text.write(f"The pasword is: {saved_password}\n")
print(f"Your data has been saved as {file_output_name}\n")
