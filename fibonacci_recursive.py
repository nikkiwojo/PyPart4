
def fibonacci(n):
    if n == 0: #base case
        return 0
    elif n == 1: #base case also
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(4))



