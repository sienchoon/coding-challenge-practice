print("Start of 100 day Coding Challenge \nToday is Day 1\n") 

#Pynative challenge for beginners
#ex1. Calculate multiplication & sum of 2 numbers
#Given two integer numbers, return their product only if 
#the product is equal to or lower than 1000. Otherwise, return their sum
print("Calculate multiplication and sum of 2 numbers")
def calculate_multiplication_or_sum(number1,number2):
    product = number1 * number2
    sum = number1 + number2
    if product <= 1000:
        return product
    else:
        return sum
    
n1 = 20
n2 = 30
print(calculate_multiplication_or_sum(n1,n2))

n1_1 = 40
n2_1 = 30
print(calculate_multiplication_or_sum(n1_1,n2_1))

#ex2. print sum of current numbers and previous numbers
#iterate first 10 numbers; range from 0 to 10

previous_num = 0
for current_number in range(0,10):
    total_sum = previous_num + current_number
    print("Current Number", current_number, "Previous Number", previous_num, "Sum:", total_sum)
    previous_num = current_number
    
    
#ex3. print characters from string that is located at even index number
string1 = "pynative"
string = "Hello World!"
def find_even_index(string):
    for i in range(0,len(string)):
        if i % 2 == 0:
            print(string[i])
            
find_even_index(string)
print("\n")
find_even_index(string1)

#ex4. remove first n characters from a string
#using slicing or indexing to remove characters from stirng

def string_remove(string, n):
    if n < 4:
        string = string[n:]
    else:
        string = string[0:n]
    return string

print(string_remove("Pynative", 5))
print("\n")

#ex5. Check if first and last num of list is same
#return value in boolean format; True or False

def first_last_same(number_list):
    first_num = number_list[0]
    last_num = number_list[-1]
    
    if first_num == last_num:
        return True
    else:
        return False
        
number_x = [10, 20, 30, 40, 10]
print("Result is:", first_last_same(number_x))
number_y = [75, 65, 35, 75, 30]
print("Result is:", first_last_same(number_y))

#ex6. Display numbers divisible by 5 from a list
Given_List = [10, 20, 33, 45, 64, 71, 85]
def divisible_by_5(list):
    divided_list = []
    for numbers in list:
        if numbers % 5 == 0:
            divided_list.append(numbers)
    return divided_list
    
new_list = divisible_by_5(Given_List)
print(new_list)

