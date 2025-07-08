def table_printer(n):
    for i in range(1, 11):
        print(f"{n} * {i} =", n * i)

n = int(input("Enter input: "))
table_printer(n)
