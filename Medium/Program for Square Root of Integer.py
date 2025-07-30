# Program for Square Root of Integer

'''
Given a positive integer n, find its square root. 
If n is not a perfect square, then return floor of √n.
'''

'''
Examples : 

Input: n = 4
Output: 2
Explanation: The square root of 4 is 2.

Input: n = 11
Output: 3
Explanation: The square root of 11 lies in between 3 and 4 so floor of the square root is 3.
'''
# My Solution
'''
def squareRoot(n):
    if n < 0:
        print("Enter Positive number: ")
    else:
        squareRootedNum = n ** (1/2)

        if squareRootedNum % 2 == 0:
            return int(squareRootedNum)
        else:
            return int(squareRootedNum // 1)
        
print("Sqaure root: ", squareRoot(16))
'''

# My optimized solution: Time Complexity O(1), for large numbers O(log n), Space O(1)
'''
def squareRoot(n):
    if n < 0:
        print("Enter Positive number: ")
    else:
        return int(n ** (1/2))

print("Sqaure root: ", squareRoot(16))
'''

#Geeks Naive Approach Loop - O(sqrt(n)) Time, O(1) Space
'''
def floorSqrt(n):

    #Interate from 1 until square exceeds n
    res = 1
    while res * res <= n:
        res += 1

    # return largest integer whose sqr
    # is <= n
    return res - 1

if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))
'''

# Geeks expected approach Binary Search - O(log(n)) Time and O(1) Space
'''
def floorSqrt(n):

    #Initial search space
    lo = 1
    hi = n
    res = 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # if sqaure of mid is <= n
        # update result and search upper half

        if mid * mid <= n:
            res = mid
            lo = mid + 1

        #If square of mid exceed n,
        #Search in lower half
        else:
            hi = mid - 1
 
    return res

if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))
'''

# Geeks alternate approach Built in functions - O(log(n)) Time, O(1) Space
'''
import math

def floorSqrt(n):

    res = int(math.sqrt(n))
    return res

n = 11
print(floorSqrt(n))
'''

#Geek alternate Forumula used by pocket calculators - O(1) Time, O(1) Space
'''
import math

def floorSqrt(n):

    res = int(math.exp(0.5 * math.log(n)))

    if (res + 1) ** 2 <= n:
        res += 1
    
    return res

n = 11
print(floorSqrt(n))
'''