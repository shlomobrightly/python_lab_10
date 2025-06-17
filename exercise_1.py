"""
Name: is_str_letters

Input: a string

Output: True or False

Algorithm:  1- if the ascii value of the first character is not in the range of "A" - "Z" or "a" - "z", returns False.
            2- elsewise, if the length on the given string is 1, returns True, otherwise, in a Recursion, returns the is_str_letters function on a new list with the first element sliced out.



Name: main()

Input: a string

Output: a message given in text

Algorithm:  1- inputs a string
            2- applies is_str_letters function on the given string, and prints a text if the function returns True, and a different text if returns False.
"""


def is_str_letters(string):
    
    # stopping condition
    if not "a" <= string[0] <= "z" and not "A" <= string[0] <= "Z": 
        return False

    # Recursion
    else:
        if len(string) == 1:
            return True
        else:    
            return is_str_letters(string[1:])
    

    
def main():

    a = input("Please enter a string: ")
    if is_str_letters(a) == True:
        print("The string is legal.")
    else:
        print("The string is illegal!")


main()    



































