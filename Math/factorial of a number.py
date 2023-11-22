def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

number = int(input("Enter number:"))

print (calculate_factorial(number))
