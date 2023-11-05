# codewars 
# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python?collection=code-gym-number-2

#Given an array of integers your solution should find the smallest integer.
#For example:
#Given [34, 15, 88, 2] your solution will return 2
#Given [34, -345, -1, 100] your solution will return -345

#work solution :  list, find min value, use min function
def find_smallest_int(arr):
    # return min(arr)
    print(f'{min(arr)}')

arr1 = [34, 15, 88, 2]
arr2 = [34, -345, -1, 100]

find_smallest_int(arr1)
find_smallest_int(arr2)


#https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python

# Is the string uppercase?
# Create a method to see whether the string is ALL CAPS.
#For Example
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True

# work solution : string must contain all uppercase. loop, if all upper, return True else, False

def is_uppercase(string):
    for char in string:
        if char == char.upper():
            return True
        else:
            return False
        