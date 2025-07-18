# The dice problem
'''
You are given a cubic dice with 6 faces. 
All the individual faces have a number printed on them. 
The numbers are in the range of 1 to 6, like any ordinary dice. 
You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.
'''
'''
Examples:

Input: n = 2
Output: 5
Explanation: For dice facing number 5 opposite face will have the number 2.

Input: n = 6
Output: 1
Explanation: For dice facing number 6 opposite face will have the number 1.
'''

#Solution ideas
'''
# If else equal to opposite
# Sum - input, output opposite
'''

#My Solution: Had a peak at the title of solutions so cheated a little: Title said use sum of two sides
'''
# Dice number: 1, 2, 3, 4, 5, 6
# Total of opposites is 7

def dice_opposite(n):
    return 7 - n

dice_input = int(input("Enter dice number for opposite: "))
print("Opposite dice number: ", dice_opposite(dice_input))
'''

# Naive Approach: If-else
'''
def dice_opposite(n):
    if n == 1:
        return 6
    if n == 2:
        return 5
    if n == 3:
        return 4
    if n == 4:
        return 5
    if n == 5:
        return 4
    if n == 6:
        return 1

n = 1
print("Dice opposite: ", dice_opposite(n))
'''

#Expected approach: using sum of two sides
'''
def dice_opposite(n):
    ans = 7 - n
    return ans

n = 2
print(dice_opposite(n))
'''
