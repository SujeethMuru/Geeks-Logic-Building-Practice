#Check if a larger number is divisible by 13 or not
'''
Given a number s represented as a string, 
determine whether the integer it represents is divisible by 13 or not.

Examples : 

Input: s = "2911285"
Output: true
Explanation: 2911285 / 13 = 223945, which is a whole number with no remainder.

Input: s = "27"
Output: false
Explanation: 27 / 13 ≈ 2.0769..., which is not a whole number (there is a remainder).
'''
#My Solution: Modulo operator
'''
def divBy13(s):
    return int(s) % 13 == 0

s = "2911285"
print(divBy13(s))
s = "27"
print(divBy13(s))
'''

def divBy13(s):
    n = int(s)

    while n > 99:
        last_digit = n % 10
        rest = n // 10

        n = rest + (4*last_digit)
    return n % 13 == 0

s = "2911285"
print(divBy13(s))
s = "27"
print(divBy13(s))
