
number = 1

while (number <= 100):
    if (number % 3 == 0 and number % 5 != 0):
        print("Fizz")
        number = number + 1
    elif (number % 5 == 0 and number % 3 != 0):
        print("Buzz")
        number = number + 1
    elif (number % 5 == 0 and number % 3 == 0):
        print("FizzBuzz")
        number = number + 1
    else:
        print(number)
        number = number + 1

