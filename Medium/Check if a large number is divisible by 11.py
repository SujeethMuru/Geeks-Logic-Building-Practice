#Check if a large number is divisible by 11 or not
'''
Given a number in the form of string s, 
Check if the number is divisible by 11 or not. 
The input number may be large 
and it may not be possible to store it even if we use long long int.
'''
'''
Examples: 

Input: s = "76945"
Output: true
Explanation: s when divided by 11 gives 0 as remainder.

Input: s = "7695"
Output: false
Explanation: s does not give 0 as remainder when divided by 11.

'''
# My Solution: Formula
'''
def check_11_divisibility(s):
    #edge case 0
    if len(s) == 0:
        return False
    
    #edge case 1
    if len(s) == 1:
        return int(s) % 11 == 0

    
    # check 11 divisbility
    odd_Num_Sum = 0
    even_Num_Sum = 0

    for i in range(len(s)):
        digit = int(s[i])
        if i % 2 == 0:
            even_Num_Sum += digit
        else:
            odd_Num_Sum += digit
    
    if abs(odd_Num_Sum - even_Num_Sum) % 11 == 0:
        return True
    
    return False

s = "76945"
print(check_11_divisibility(s)) #True
s = "7695"
print(check_11_divisibility(s)) #False
s = "1234567589333892"
print(check_11_divisibility(s)) #True
'''    
def divBy11(s):

    #Convert string to int
    n = int(s)
    return n % 11 == 0

if __name__ == "__main__":
    s = "76945"

    if divBy11(s):
        print("True")
    else:
        print("False")

    