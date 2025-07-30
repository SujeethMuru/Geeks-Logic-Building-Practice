# Check if a number is a power of another number

'''
Given two positive numbers x and y, 
check if y is a power of x or not.
'''

'''
Examples: 

Input:  x = 10, y = 1
Output: True
x^0 = 1

Input:  x = 10, y = 1000
Output: True
x^3 = 1

Input:  x = 10, y = 1001
Output: False
'''

#My Iterative Solution: Time O(log y), Space O(1)
'''
def powerChecker(x, y):
    num = x
    power = y
    dividedPower = power

    if y == 1: #Base case for 0
        return True
    
    while dividedPower > 1:
        
        if dividedPower % x == 0:
            dividedPower = dividedPower / num

        else:
            return False
        
    return True

print(powerChecker(10, 1001))
'''

# My Logarithmic approach: AI assisted Time O(1), Space O(1)

    # formula log_x(y) = n, n = log_10(y)/log_10(x) or ln(y)/ln(x)
import math
def powerChecker(x, y):
    n = math.log(y)/math.log(x)

    if abs(n - round(n)) < 1e-10:
        return True
    
    return False

print(powerChecker(10, 10001))



