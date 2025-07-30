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
'''
import math
def powerChecker(x, y):
    n = math.log(y)/math.log(x)

    if abs(n - round(n)) < 1e-10:
        return True
    
    return False

print(powerChecker(10, 10001))
'''

# Geek Naive approach Repeated multiplcation method: Time O(log_x y), Space O(1)
'''
def isPower(x, y):

    if x == 1:
        return y == 1
    
    pow = 1
    while pow < y:
        pow *= x

    return pow == y

print(isPower(10, 1))
print(isPower(2, 30))
'''

# Geek better approach Exponentiation and Binary Search method Time O(log log y), Space O(1)
'''
import math
def isPower(x, y):
    if x == 1:
        return y == 1
    
    if y == 1:
        return 1
    pow = x

    while pow < y:
        pow *= x

    if pow == y:
        return True
    
    low, high = x, pow
    while low <= high:
        mid = low + (high - low) // 2
        result = int(x ** int(math.log(mid) / math.log(x)))

        if result == y:
            return True
        if result < y:
            low = mid + 1
        else:
            high = mid - 1

    return False

print("true" if isPower(10, 1) else "false")
print("true" if isPower(1, 20) else "false")
'''

# Geeks Expected Logarithmic method Time O(1), Space O(1)
import math

def isPower(x, y):
    res1 = math.log(y) / math.log(x)
    return res1 == math.floor(res1)

print(isPower(2, 128))