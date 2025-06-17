"""

Name: is_palindrom

Input: a list

Output: True or False

Algorithm:  1- if the length of the list is smaller than 2, returns True.
            2- othewise, if the first character of the number is equal to the last character, returns a Recursion of is_palindrom function on the given list with sliced out first and last characters.
            3- if the first character is not eqal to the last, returns False.
            
            
            
Name: main():

Input: a number

Output: text depending on if is_palindrom function returns True or False

Algorithm:  1- temporarely starts "a" as 10
            2- prints a text
            3- in a while loop, as long as not given 0, creates a empty list and inputs a number. if inputs 0, prints text and exits program.
            4- stats b as a. and in a while loop, as long as larger than 9, appends the ones digit to the created list, and shortens b by dividing by wholes.
            5- if smaller than 10, appends b to the list
            6- applies is_palindrom function on the created list. and prints text according if returns True or False
"""



def is_palindrom(lst):
    # stop condition
    if len(lst) <= 2:
        return True
    if lst[0] == lst[len(lst) - 1]:
        return is_palindrom(lst[1:len(lst)-1:])
    else:
        return False
        
        
def main():
    
    a = 10 #temporarely
    print("Enter a sequence of natural numbers,end with 0:")
    while a != 0:
        lst = []
        a = int(input())
        if a == 0:
            print("FINISH")
            return
        b = a 
        while b > 9:
            lst.append(b%10)
            b //= 10
        if b < 10:
            lst.append(b%10)
        if is_palindrom(lst) == True:
            print("The list of digits is a Palindrom")
        else:
            print("The list of digits is not a Palindrom")


main()    
