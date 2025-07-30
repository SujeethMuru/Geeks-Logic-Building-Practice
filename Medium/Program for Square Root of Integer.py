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
# My optimized solution:
def squareRoot(n):
    if n < 0:
        print("Enter Positive number: ")
    else:
        return int(n ** (1/2))

print("Sqaure root: ", squareRoot(16))