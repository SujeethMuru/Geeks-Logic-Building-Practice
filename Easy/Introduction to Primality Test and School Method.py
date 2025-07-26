import math
#Introduction to Primality Test and School Method

'''
Given a positive integer, check if the number is prime or not. 
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Examples of the first few prime numbers are {2, 3, 5, ...}

Examples : 

Input:  n = 11
Output: true

Input:  n = 15
Output: false

Input:  n = 1
Output: false 
'''
#My Solution

def prime_finder(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True
    
    
print(prime_finder(15)) #False
print(prime_finder(2))  #True
print(prime_finder(1))  #False
print(prime_finder(-1)) #False

