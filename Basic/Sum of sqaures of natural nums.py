#Given positive integer n, find the sum of squares of first n natural numbers.
"""
Input : n = 2
Output: 5
Explanation: 1^2+2^2 = 5

Input : n = 8
Output: 204
Explanation :  1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 = 204 
"""
# loop method
"""
def sqaures_natural_num(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
        print(total)

if __name__ == "__main__":
    n = 8
    sqaures_natural_num(n)
"""

#Efficient method
def sqaures_natural_num(n):
    return n* ((n + 1) * ((2 * n) + 1)) / 6

if __name__ == '__main__':
    n = 4
    print(sqaures_natural_num(n))
