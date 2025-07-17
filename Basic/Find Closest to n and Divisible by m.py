#Find Closest to n and Divisible by m
'''
Given two integers n and m (m != 0). 
Find the number closest to n and divisible by m. 
If there is more than one such number,
then output the one having maximum absolute value.

Examples: 

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15, 
but -18 has the maximum absolute value.
'''

#MY SOLUTION
'''
def find_closest_to_n_divisible_by_m(n, m):
    list_lesser_n= []
    list_greater_n = []

    #Fix for index error when n is already divisible by m
    if n % m == 0:
        print(f"{n} is divisible by {m}")
        print(f"Output: {n} ")
        return

    n_less = n
    while n_less % m != 0:
        list_lesser_n.append(n_less-1)
        n_less -= 1
    
    n_greater = n
    while n_greater % m != 0:
        list_greater_n.append(n_greater+1)
        n_greater += 1

    print("Numbers less than n divisible by m: ", list_lesser_n)
    print("Numbers greater than n divisible by m: ", list_greater_n)
    print(f"Input: n = {n}, m = {m}")

    return_closest_numbers(list_lesser_n, list_greater_n)


def return_closest_numbers(list_lesser, list_greater):
    if len(list_lesser) < len(list_greater): #lesser number prints
        print(list_lesser[-1])
    elif len(list_lesser) == len(list_greater): #if length is equal output maximum absolute value
        left_pos_num = abs(list_lesser[-1])
        right_pos_num = abs(list_greater[-1])

        if left_pos_num < right_pos_num:
            print(list_greater[-1])
        else:
            print(list_lesser[-1])

    else: # printer greater number divisble by m
        print(list_greater[-1])
        
    
if __name__ == "__main__":
    n = -12
    m = 6

    find_closest_to_n_divisible_by_m(n, m)
'''

#Iterative approach
'''
def closest_number(n, m):

    closest = 0 
    min_difference = float('inf') # comparing using positive infinity

    #Checking numbers around n
    for i in range (n - abs(m), n + abs(m) + 1):

        if i % m == 0:
            difference = abs(n - i)

            if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference 
    return closest

if __name__ == "__main__":
    n = 13
    m = 4
    print(closest_number(n, m))
'''

#Expected approach
def closestNumber(n, m) :
    #get quotient
    q = int(n/m)

    #closest multiple of m that is less than or = to n.
    n1 = m * q #Dividend * quotient

    # 2nd possible closest number
    if((n*m) > 0):
        n2 = (m * (q + 1))
    else:
        n2 = (m * (q - 1))

    #If true, then n1 is the required closest number
    if (abs(n - n1)) < abs(n - n2) :
        return n1
    
    #Else n2 is the closest number
    return n2

if __name__ == "__main__":
    n = 16; m =4
    print(closestNumber(n,m))