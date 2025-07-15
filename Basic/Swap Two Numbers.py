# Given two numbers a and b, the task is to swap them.
''' INSTRUCTIONS
Input: a = 2, b = 3
Output: a = 3, b = 2

Input: a = 20, b = 0
Output: a = 0, b = 20

Input: a = 10, b = 10
Output: a = 10, b = 10 
'''

''' MY SOLUTION
USER INPUT
input_a = int(input("Enter integer input a = "))
input_b = int(input("Enter integer input b = "))
def swap(a, b):
    input_list = [a, b]
    print(f"Unswapped Output: a = {input_list[0]}, b = {input_list[1]}")
    input_list[0] = b
    input_list[1] = a
    print(f"Swapped Output: a = {input_list[0]}, b = {input_list[1]}")
    
#swap(input_a, input_b)

#Hardcoded input
if __name__ == "__main__":
    input_a = 2
    input_b = 3

swap(input_a, input_b)
'''

'''
# [NAIVE APPROACH] USING THIRD VARIABLE
if __name__ == "__main__":
    a = 2
    b = 3
    print(f"Unswapped Output: a = {a}, b = {b}")

    temp = a
    a = b
    b = temp
    print(f"Swapped Output using temp variable: a = {a}, b = {b}")
'''
# SWAPPING WITHOUT USING 3RD VARIABLE
''' #ARITHEMTIC APPROACH
input_a = int(input("Enter input a: "))
input_b = int(input("Enter input b: "))

#Arithmetic swapping
def swap_with_third_variable(a, b):
    print(f"Unswapped Output: a = {a}, b = {b}")

    # Swapping without third variable
    a = a + b
    b = a - b
    a = a - b
    
    print(f"Swapped Output: a = {a}, b = {b}")

swap_with_third_variable(input_a, input_b)
'''

# USING BITWISE XOR OPERATOR

'''
# [ALTERNATE APPROACH] BUILT IN SWAP
if __name__ == "__main__":
    a = 2
    b = 3
    print(f"Unswapped Output: a = {a}, b = {b}")

    a, b = b, a
    print(f"Swapped Output: a = {a}, b = {b}")
'''





