# Nth term of AP from First Two Terms
'''
Given two integers a1 and a2, 
the first and second terms of an Arithmetic Series respectively, 
the problem is to find the nth term of the series. 
'''

'''
Examples :

Input : a1 = 2,  a2 = 3,  n = 4
Output : 5
Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

Input : a1 = 1, a2 = 3, n = 10
Output : 19
Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.
'''

#My for loop Solution: Used Asisstance from ChatGPT so not completly mine
'''
def nth_term(a1, a2, n):
    difference = a2 - a1
    term = a1

    for i in range(1, n):
        term += difference
        print(term)
    
    return term


a1 = 2
a2 = 3
n = 4
print("Output: ", nth_term(a1, a2, n))
'''

#My formula Solution: Formula for nth term from ai: a_n = a_1 + (n-1) * d
'''

def nth_term(a1, a2, n):
    d = a2 - a1
    nth = a1 + (n-1) * d

    return nth

    a1 = 2
    a2 = 3
    n = 4
    print("Output: ", nth_term(a1, a2, n))

    a1 = 1
    a2 = 3
    n = 10
    print("Output: ", nth_term(a1, a2, n))

'''

#Naive approach: For loop
'''
def nth_term(a1, a2, n):
    nthTerm = a1
    d = a2 - a1

    for i in range(1, n):
        nthTerm += d 
    return nthTerm

a1 = 2
a2 = 3
n = 4
print(nth_term(a1, a2, n))

'''

# Expected Approach
'''
def nth_term(a1, a2, n):
    return a1 + (n - 1) * (a2 - a1)

a1 = 2
a2 = 3
n = 4
print(nth_term(a1, a2, n))
'''
