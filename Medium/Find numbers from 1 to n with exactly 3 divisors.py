# Find numbers from 1 to n with exactly 3 divisors

'''
Given a number n, print all numbers in the range from 1 to n 
having exactly 3 divisors. 
'''
'''
Examples: 

Input: n = 16
Output: 4 9
Explanation: 4 and 9 have exactly three divisors.

Input: n = 49
Output: 4 9 25 49
Explanation: 4, 9, 25 and 49 have exactly three divisors.
'''

# My solution using while loop: failed due to lack of understanding problem
'''
def countDivisor(n):
    divisor_count = 0
    divisor_list = []

    while divisor_count <= 3:
        for i in range (1, n+1):
            if n % i == 0:
                divisor_count += 1
                divisor_list.append(i)
    
    return divisor_list

print(countDivisor(49)) # output = [1, 7, 49, 1, 7, 49]
'''

# My solution assistance from AI
#Numbers with exactly 3 divisors are squares of prime numbers
import math
def countDivisor(n):
    