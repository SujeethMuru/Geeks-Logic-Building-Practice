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
'''
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
'''

#Geeks School Approach
'''
def isPrime(n):
    
    #Corner case
    if n <= 1:
        return False
    
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

print("True") if isPrime(11) else print("False")    #Output: True
print("True") if isPrime(14) else print("False")    #Output: False
#Time Complexity: O(n)
#Auxillary Space: O(1)
'''

#Geeks optimized school method
'''
#import math

def isPrime(n):

    #Corner case
    if (n <= 1):
        return False
    
    # Check from 2 to sqrt of n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

print("True") if isPrime(11) else print("False")    #Output: True
print("True") if isPrime(15) else print("False")    #Output: False
#Time Complexity: O(math.sqrt(n))
#Auxillary Space: O(1)
'''

#Geek More Optimized sqrt approach

#import math

def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    
    #To check through all numbers of the form 6k + 1
    # Until  i <= square root of n, with step value 6
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
        
    return True

print(isPrime(11))
print(isPrime(20))

#Time Complexity: O(sqrt(n))
#Auxillary space: O(1)








