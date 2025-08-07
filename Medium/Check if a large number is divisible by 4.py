#Check if a large number is divisible by 4 or not

'''
Given a number, the task is to check if a number is divisible by 4 or not. 
The input number may be large 
and it may not be possible to store even if we use long long int.
'''

#My Solution: % operator. Time - O(logn), Space - O(1)
'''
def check_4_divisibility(n):
    if n % 4 == 0:
        return True
    
    return False

n = 363588395960667043875487
print("Yes" if check_4_divisibility(n) is True else "No")
'''
#Geeks Modulo: Time- O(1), Space- O(1) 
'''
n = 1234567589333862
if int(n)%4==0:
    print("Yes")
else:
    print("No")
'''
#Geek Checking divisibility of Last 2 digits. Time - O(1), Space O(1)
'''
def check(st):
    n = len(st)

    if n == 0:
        return False

    if n == 1:
        return (int(st[0]) % 4 == 0)

    last = int(st[n - 1])
    second_last = int(st[n - 2])

    return ((second_last * 10 + last) % 4 == 0)

st = "76952"

if check(st):
    print("Yes")
else:
    print("No")
'''

#Geeks Substirng to Integer. Time - O(1), Space - O(1)
'''
def check(s):

    if len(s) == 0:
        return False
    if len(s) == 1:
        return  int(s) % 4 == 0
    
    return int(s[-2:]) % 4 == 0

s = "76952"

print("Yes" if check(s) else "no")
'''


    

