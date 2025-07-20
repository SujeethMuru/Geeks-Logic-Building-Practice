# SUM OF DIGITS OF A NUMBER
# Given the number n, find the sum of its digits

'''
Examples : 

Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21

Input: n = 12
Output: 3
Explanation: The sum of its digits are: 1 + 2 = 3
'''
#Ideas
'''
Loop through num #Failed: Int cannot be iterated over
Use list separate each number 
Use range function
'''

#Failed Attempt: Loop through num
'''
def sumOfDigits(num):
    sum = 0
    for n in num:
        print(n)
        sum += n

    return num

if __name__ == "__main__":
    n = 687
    print("Output: ", sumOfDigits(n))   #Output should equal 21
'''

# My Working Solution: Idea after looking up how to iterate using ints
'''
def sumOfDigits(num):
    sum = 0
    for digit in str(num):
        #print(digit)  To see digits being iterated over
        sum += int(digit)
    
    return sum

if __name__ == "__main__":
    n = 687
    print("Output:", sumOfDigits(n))   #Output should equal 21

    n = 12
    print("Output:", sumOfDigits(n))   #Output should equal 3
'''

# Digit Extraction Approach
'''
def sumOfDigits(n):
    sum = 0 
    while n != 0:

        #extract last digit
        last = n % 10

        #add last digit
        sum += last

        #remove last digit
        n //= 10
    return sum

if __name__ == "__main__":
    n = 12345
    print(sumOfDigits(n)) #Output should equal 15
'''

# Approach 2: Recursive method - Function calls itself

'''
def sumOfDigits(n):
    # Base Case
    if n == 0 :
        return 0
    
    #Recursive Case
    return n % 10 + sumOfDigits(n // 10)
        #Self Notes
        # 12345 % 10 + sumOfDigits(12345 // 10)
            # 5      + sumOfDigits(1234)
                        # 4     +   sumOfDigits(1234)
                                        # 3         +   sumOfDigits(123) and so on
print(sumOfDigits(12345))
'''
