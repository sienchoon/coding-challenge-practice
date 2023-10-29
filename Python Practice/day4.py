#learning functions through CS50X 
def main_body():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main_body() #calling the function


def print_hello_world():
    print("Hello World")
    
print_hello_world() #calling the function



