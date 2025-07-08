def odd_or_even(n):
    rem = n % 2
    if rem == 0:
        print("Output: True")
        print(f"Explanation: {n} % 2 = 0, so {n} is even.")
    else:
        print("Output: False")
        print(f"Explanation: {n} % 2 = 1, so {n} is odd.")

n = int(input("Enter input: " ))
odd_or_even(n)