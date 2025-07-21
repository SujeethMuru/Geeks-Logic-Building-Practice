# Write a program to reverse digits of a number
# Given an Integer n, find the reverse of its digits.
'''
Examples:
Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.

Input: n = 200
Output: 2
Explanation: By reversing the digits of number, number will change into 2.

Input: n = 12345 
Output: 54321
Explanation: By reversing the digits of number, number will change into 54321.
'''
#Ideas
'''
int to string conversion. Concatenate string then return int.
Digit extraction
'''
# My Soultion: String conversion 
'''
def reverseDigits(num):
    string_num = str(num)
    reverse_num = []
    for n in string_num:
        reverse_num.append(string_num[-1])
        print(reverse_num)
        string_num.replace(string_num[-1], "")
        print(reverse_num)

    return reverse_num            

print(reverseDigits(122))
'''
#My Solution: Digit extraction 
'''
def reverseDigits(num):
    reversed_digits = 0
    if num >= 0:
        while num != 0:

            #Last digit extracition
            last_digit = num % 10

            #Reversing digit : Got aid from ai for this formula
            reversed_digits = reversed_digits * 10 + last_digit
            
            #Last digit removal
            num //= 10

        return reversed_digits
    
    else: # For negative number
        num *= -1
        while num != 0:

            #Last digit extracition
            last_digit = num % 10

            #Reversing digit : Got aid from ai for this formula
            reversed_digits = reversed_digits * 10 + last_digit
            
            #Last digit removal
            num //= 10

        return reversed_digits * -1

print(reverseDigits(-12345))
'''

#My Solution: Digital extraction simplified
def reverseDigits(num):
    absolutle_num = abs(num)
    reversed_digits = 0

    while absolutle_num != 0:

        #Last digit extracition
        last_digit = absolutle_num % 10

        #Reversing digit : Got aid from ai for this formula
        reversed_digits = reversed_digits * 10 + last_digit
        
        #Last digit removal
        absolutle_num //= 10

    #More simplified if else
    return reversed_digits if num >= 0 else -reversed_digits

    '''
    if num >= 0:
        return reversed_digits
    else:
        return reversed_digits * -1
    '''

print(reverseDigits(-12345))




        