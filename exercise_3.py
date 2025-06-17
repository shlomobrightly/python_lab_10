"""

Name: is_prefix

Input: two strings (st, pre_st)

Output: True or False

Algorithm:  1- if either st or pre_st is equal to a empty string, reutns False
            2- otherwise, if pre_st is equal to the firsrt character of st, returns False. (stopping condition)
            3- if the first character of pre_st is equal to the firsrt character of st, in a recursion, apply the is_prefix function on the two given strings with the first characters sliced out.
            4- elsewise, returns False



Name: main()

Input: two strings (st, pre_st)

Output: text depending wether the is_prefix function returns True or False

Algorithm:  1- ipnuts two strings  (st, pre_st)
            2- applies the is_prefix function on the strings, and prints text depending wether the is_prefix function returns True or False

"""


def is_prefix(st, pre_st):

    if pre_st == "" or st == "":
        return False
    
    # stop condition
    if pre_st == st[0]:
        return True
    
    if st[0] == pre_st[0]:
        return is_prefix(st[1::], pre_st[1::])
    else:
        return False
        
        
def main():
    st = input("Enter a string:")
    pre_st = input("Enter another string:")
    
    if is_prefix(st, pre_st):
        print(pre_st, "is a prefix of", st)
    else:
        print(pre_st, "is not a prefix of", st)
    
main()    
