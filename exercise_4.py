"""

Name: check_num

Input: a string of numbers

Output: number that resemblse the string

Algorithm:  1- applies "num" as 0
            2- if the lenght of the given string is smaller or equal to zero, returns num (stop condition)
            3- subtracts the ascii value of "0" from the ascii value of the first character of the string. then multiplies the result by 10 in the power of the lenght of the string minus 1.
            4- adds up the resulst above to "num"
            5- in a recursion, applies the check_num function on the list with the first character sliced out, considering "num" with its current value.
            
            
Name: main():

Input: a string

Output:  a text with the number that resemblse the string, or text if the string is not made only of numbers

Algorithm:  1- inputs a string
            2- in a for loop in the given string, if found a character not in the ascii range of "0" - "9", prints a text and exist the loop.
            3- if not found a character not in the ascii range of "0" - "9", prints a text with the number that resemblse the string
"""

def check_num(st, num = 0):
    
    # stop condition
    if len(st) <=0:
        return num
    
    num += (ord(st[0])-ord("0"))*10**((len(st))-1)
    return check_num(st[1::],num)
    
    

        
def main():
    
    st = input("Please enter a string: ")
    for i in st:
        if not "0" <= i <="9":
            print("The string is illegal!")
            return
        
    print("The string",st ,"corresponds to the number", check_num(st),".")        
    
main()    
        
        
