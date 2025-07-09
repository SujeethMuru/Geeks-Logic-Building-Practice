'''
Given a positive integer n, find the sum of the first n natural numbers.
positive number > 0
natural number = set of postive numbers

Input n=3
Output: 6
Explanation: 1 + 2 + 3 = 6

Input: n = 5
Output: 15 
Explanation:  1 + 2 + 3 + 4 + 5 = 15

Inputs have to positive
outputs have to count up to n and add all the number including n
'''
# for loop method (naive approach)
"""
def sum_of_natural_nums(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

if __name__ == '__main__':
    n = 3
    print(f"Output: {sum_of_natural_nums(n)}")

    n = 5
    print(f"Output: {sum_of_natural_nums(n)}")

    n = 7
    print(f"Output: {sum_of_natural_nums(n)}")
"""

#(Efficient method)
def sum_of_natural_nums(n):
    return (n*(n+1))//2

if __name__ == '__main__':
    n = 3
    print(f"Output: {sum_of_natural_nums(n)}")

    n = 5
    print(f"Output: {sum_of_natural_nums(n)}")

    n = 7
    print(f"Output: {sum_of_natural_nums(n)}")

