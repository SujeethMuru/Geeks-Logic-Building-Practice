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

    while string_num != "":
        reverse_num.append(string_num[-1])
        string_num = string_num[:-1]
        print(reverse_num)

    reverse_num = "".join(reverse_num)
    reverse_num = int(reverse_num)
    return reverse_num            

print(reverseDigits(221))

#Time Complexity: O((log n)**2)
#Space Complexity: O(d) or O(log n)
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
'''
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

    #simplified if else
    return reversed_digits if num >= 0 else -reversed_digits

print(reverseDigits(123))

#Time Complexity: O(log n)
#Space Complexity: O(1)
'''

# Geeks Approach: Digit by Digit
'''
n = 4562
rev = 0

while (n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev) #Output was 2654

#Time complexity - O(log n)
#Space complexity - O(1)
'''
#Geeks Recursive Approach
'''
def reverseDigits(n, revNum, basePos):
    if n > 0:
        reverseDigits(n//10, revNum, basePos)
        revNum[0] += (n % 10) * basePos[0]
        basePos[0] *= 10

#Driver code
n = 4562
revNum = [0]
basePos = [1]
reverseDigits(n, revNum, basePos)
print(revNum[0])

#Time Complexity: O(log n)
#Space Complexity: O(log n)
'''

#Geeks String to list reversal Approach
'''
def reverseDigits(n):

    # converted number to string
    s = str(n)

    # reverse the string
    s = list(s)
    s.reverse()
    s = "".join(s)

    # converting string to interger
    n = int(s)
    return n

num = 4562
print(reverseDigits(num)) 

#Time Complexity O(log n)
#Space Copmlexity O(1)
'''

#Geeks String Slicing approach
'''
def reverseDigits(n):

    # convert num to int
    s = str(n)
    
    # Reversing string
    s = s[::-1]

    # convert string to int
    n = int(s)

    return n

n = 4562
print(reverseDigits(n))

#Time complexity - O(n)
#Space complexity - O(n)
'''