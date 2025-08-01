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

# My solution assistance from AI, Time O(n^3/4), space O(sqrt(n))
#Numbers with exactly 3 divisors are squares of prime numbers
'''
import math

def prime_finder(n): #Reusing prime function from easy problem
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True


def findThreeDivisor(n): #Find all prime numbers and square them
    divisible_by_three = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_finder(i) == True:
            sqaured = i ** 2
            divisible_by_three.append(sqaured)

    return divisible_by_three

print(findThreeDivisor(100))
'''
# Geeks Naive: Nested Loop, Time o(n^2), space O(1)
'''
def count_divisors(n): #count divisors of a number using two loops

    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def numbers_with_3_divisors(n):

    for i in range(1, n + 1):
        if count_divisors(i) == 3:
            print(i, end=' ')

n = 100
print(f"#s with exactly 3 divisors up to {n} are:")
numbers_with_3_divisors(n)
'''

#Geeks Expected: Mathematical approach Time o(n*log(log(n))), O(n)
'''
def numbersWith3Divisors(n):

    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    p = 2
    while (p*p <= n):

        # if prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):

            #Update all multiples of p
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    
    # print squres of primes upto n.
    i = 0
    while (i*i <= n):
        if (prime[i]):
            print(i*i, end=" ")
        i += 1

# Driver code
n = 96
numbersWith3Divisors(n)
'''
#Geeks Expected 2: Constant Space. Time: O(n**(3/4)), Space O(1)
# Python3 program to print all
# three-primes smaller than
# or equal to N without using
# extra space

# 3 divisor logic implementation
# check if a number is  prime or
# not if it is a prime then check
# if its square is less than or
# equal to the given number


def numbersWith3Divisors(n):

    print("Numbers with 3 divisors : ")

    i = 2
    while i * i <= n:

        # Check prime
        if (isPrime(i)):
                # Print numbers in the order
                # of occurrence
                print(i * i, end=" ")

        i += 1

# Check if a number is prime or not


def isPrime(n):

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


# Driver code
if __name__ == "__main__":
    n = 122

    # Function call
    numbersWith3Divisors(n)

