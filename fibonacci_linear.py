
sequence = [0, 1]
count = 0

while count <= 100:
    sequence.append(sequence[count]+sequence[count + 1])
    count = count + 1

def fibonacci(n):
    
    if n >= 0:
        print(sequence[n])
    else:
        print("invalid input")

value = int(input("Please enter which part of the fibonacci sequence you would like to see."))
fibonacci(value)
