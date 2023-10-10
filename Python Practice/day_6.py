string = input("Enter a word of choice: ")
even_strings = []
def get_even_strings(string):
    for even_index in string:
        if even_index % 2 == 0:
            even_strings.append(even_index)
    return even_strings