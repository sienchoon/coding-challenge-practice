# user_input = input("Enter a word of choice: ")
# even_characters = []
# def get_even_characters(input_string):
#     for index in range(len(input_string)):
#         if index % 2 == 0:
#             even_characters.append(input_string[index])
#     return even_characters

# if len(user_input) == 0:   
#     print("Please enter a valid word...")
# else:
#     print("The even characters in the words:", ''.join(user_input))
    
user_input = input("Enter a word of choice: ")
even_characters = []

def get_even_characters(input_string):
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            even_characters.append(char)
    return even_characters

if len(user_input) == 0:
    print("Please enter a valid word.")
else:
    even_characters = get_even_characters(user_input)
    print("Even characters in the word:", ''.join(even_characters))
