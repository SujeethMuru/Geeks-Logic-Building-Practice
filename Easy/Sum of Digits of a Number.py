# SUM OF DIGITS OF A NUMBER
# Given the number n, find the sum of its digits

'''
Examples : 

Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21

Input: n = 12
Output: 3
Explanation: The sum of its digits are: 1 + 2 = 3
'''
#Ideas
'''
Loop through num #Failed: Int cannot be iterated over
Use list separate each number 
Use range function
'''

#Failed Attempt: Loop through num
"""
def sumOfDigits(num):
    sum = 0
    for n in num:
        print(n)
        sum += n

    return num

if __name__ == "__main__":
    n = 687
    print("Output: ", sumOfDigits(n))   #Output should equal 21
"""

# Idea after looking up how to iterate using ints
def sumOfDigits(num):
    sum = 0
    for digit in str(num):
        #print(digit)  To see digits being iterated over
        sum += int(digit)
    
    return sum

if __name__ == "__main__":
    n = 687
    print("Output:", sumOfDigits(n))   #Output should equal 21

    n = 12
    print("Output:", sumOfDigits(n))   #Output should equal 3