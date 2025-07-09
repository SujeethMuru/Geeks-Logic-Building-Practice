# loop / iterative method
"""
def table_printer(n):
    for i in range(1, 11):
        print(f"{n} * {i} =", n * i)

n = int(input("Enter input: "))
table_printer(n)
"""
# Recursive method (function calls itself)

def table_printer(n, i = 1):
    if i > 10: #base case
        return
    print(f"{n} * {i} = {n*i}")
    i += 1
    table_printer(n, i)

if __name__ == '__main__':
    n = 3
    table_printer(n)
