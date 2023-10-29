#learning functions through CS50X 
# calling functions 
def meow_program():
    number = get_number() #variable is assigned to the function
    meow(number) #function is called with assigned argument
    
def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):   # _ is a place holder variable 
        print("Meow")

meow_program() #calling the function


# getting to know you function
def who_am_i():
    name = full_name()
    print(name)


def full_name():
    while True:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        if first_name.isalpha() and last_name.isalpha():
            break
    first_name = first_name.title()
    last_name = last_name.title()
    return f"My name is {first_name} {last_name}" #returning first_name, last_name

who_am_i()
