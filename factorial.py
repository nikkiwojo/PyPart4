
def factorial(n):
    if n == 0: #base case
        return 1
    elif n == 1: #base case also
        return 1
    else:
        return n * factorial(n - 1)

print("5! =", factorial(5))
